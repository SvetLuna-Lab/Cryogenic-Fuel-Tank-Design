# src/compare_materials.py
from .tank_config import Material, Insulation, CryoTankConfig
from .boiloff_model import tank_shell_mass, boiloff_rate

def main():
    # Общая геометрия и пропеллент
    radius = 2.0
    height = 8.0
    p_int = 3e5

    prop_name = "LOX"
    rho = 1140.0
    latent = 213e3

    mli = Insulation(
        name="MLI + vacuum jacket",
        heat_leak_W_per_m2=1.0
    )

    al_li = Material("Al-Li 2195", density=2700.0, yield_strength=450e6, safety_factor=1.5)
    cfrp  = Material("CFRP tank (concept)", density=1600.0, yield_strength=900e6, safety_factor=2.0)

    configs = []
    for mat in (al_li, cfrp):
        cfg = CryoTankConfig(
            propellant_name=prop_name,
            propellant_density=rho,
            latent_heat=latent,
            radius=radius,
            cyl_height=height,
            internal_pressure=p_int,
            material=mat,
            insulation=mli,
        )
        configs.append(cfg)

    print("=== Material comparison (same geometry) ===")
    for cfg in configs:
        mass = tank_shell_mass(cfg)
        m_boil = boiloff_rate(cfg)
        print(f"{cfg.material.name:24s}  shell mass = {mass:8.1f} kg, "
              f"boil-off = {m_boil:6.3f} kg/h")

    print("\nNote: CFRP mass is lower, but real designs require liner, "
          "complex QA and qualification, and have higher technical risk.")

if __name__ == "__main__":
    main()
