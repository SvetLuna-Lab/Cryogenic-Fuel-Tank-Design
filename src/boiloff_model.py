"""
Simple boil-off and shell-mass estimation for a cryogenic tank.

Usage:
    python -m src.boiloff_model
"""

import math
from .tank_config import Material, Insulation, CryoTankConfig

SECONDS_PER_HOUR = 3600.0

def tank_surface_area(radius: float, cyl_height: float) -> float:
    """
    Surface area of cylinder + 2 hemispherical domes.
    """
    area_cyl = 2 * math.pi * radius * cyl_height
    area_sphere = 4 * math.pi * radius**2  # two hemispheres = full sphere
    return area_cyl + area_sphere

def tank_volume(radius: float, cyl_height: float) -> float:
    """
    Volume of cylinder + 2 hemispherical domes.
    """
    vol_cyl = math.pi * radius**2 * cyl_height
    vol_sphere = 4/3 * math.pi * radius**3
    return vol_cyl + vol_sphere

def shell_thickness(config: CryoTankConfig) -> float:
    """
    Very simplified hoop stress estimate for cylindrical section:
    sigma = p * r / t  ->  t = p * r / (sigma_allow)
    """
    sigma_allow = config.material.yield_strength / config.material.safety_factor
    t = config.internal_pressure * config.radius / sigma_allow
    return t

def tank_shell_mass(config: CryoTankConfig) -> float:
    t = shell_thickness(config)
    area = tank_surface_area(config.radius, config.cyl_height)
    volume_shell = area * t
    return volume_shell * config.material.density

def heat_leak(config: CryoTankConfig) -> float:
    """
    Approximate total heat leak [W] through insulation.
    """
    area = tank_surface_area(config.radius, config.cyl_height)
    return area * config.insulation.heat_leak_W_per_m2

def boiloff_rate(config: CryoTankConfig) -> float:
    """
    Estimate boil-off rate [kg/hour] from heat leak and latent heat.
    """
    Q_dot = heat_leak(config)  # W = J/s
    m_dot = Q_dot / config.latent_heat  # kg/s
    return m_dot * SECONDS_PER_HOUR     # kg/hour

def demo():
    # Baseline properties for LOX (примерные значения)
    lox_density = 1140.0       # kg/m^3
    lox_latent = 213e3         # J/kg

    # Baseline material: Al-Li 2195 (очень грубо)
    al_li = Material(
        name="Al-Li 2195",
        density=2700.0,
        yield_strength=450e6,   # Pa at cryo
        safety_factor=1.5,
    )

    # Effective insulation (MLI + supports)
    mli = Insulation(
        name="MLI + vacuum jacket",
        heat_leak_W_per_m2=1.0  # W/m^2 (примерная цифра)
    )

    config = CryoTankConfig(
        propellant_name="LOX",
        propellant_density=lox_density,
        latent_heat=lox_latent,
        radius=2.0,             # m
        cyl_height=8.0,         # m
        internal_pressure=3e5,  # Pa (≈3 bar)
        material=al_li,
        insulation=mli,
    )

    shell_mass = tank_shell_mass(config)
    Q_dot = heat_leak(config)
    m_dot_h = boiloff_rate(config)

    print(f"=== Cryogenic Tank Demo ({config.propellant_name}) ===")
    print(f"Shell mass:           {shell_mass:8.1f} kg")
    print(f"Heat leak:            {Q_dot:8.1f} W")
    print(f"Boil-off rate:        {m_dot_h:8.3f} kg/hour")

if __name__ == "__main__":
    demo()
