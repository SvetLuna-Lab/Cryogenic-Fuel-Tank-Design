from dataclasses import dataclass

@dataclass
class Material:
    name: str
    density: float        # kg/m^3
    yield_strength: float # Pa (at cryogenic temperature)
    safety_factor: float  # dimensionless

@dataclass
class Insulation:
    name: str
    heat_leak_W_per_m2: float  # W/m^2, effective heat flux through MLI + supports

@dataclass
class CryoTankConfig:
    """
    Simple cylindrical tank with two hemispherical domes.
    Geometry is approximated by radius + cylindrical height.
    """
    propellant_name: str
    propellant_density: float   # kg/m^3
    latent_heat: float          # J/kg (boil-off)
    radius: float               # m
    cyl_height: float           # m
    internal_pressure: float    # Pa (gauge or absolute as per convention)

    material: Material
    insulation: Insulation
