# `src/` – Python model for cryogenic tank design

This folder contains a small, self-contained Python model that links
simple analytical formulas with the engineering concept of a cryogenic
LOX/LH₂ tank for launch vehicles.

The code is **educational** and is not intended for certified flight
hardware. It illustrates how geometry, materials, insulation and boil-off
behaviour can be explored in a reproducible way.

---

## Files

### `tank_config.py`

Defines basic data structures and configuration for the tank:

- `Material` – name, density, yield strength, safety factor.  
- `Insulation` – name, effective heat leak \[W/m²].  
- `CryoTankConfig` – propellant properties, radius, cylindrical height,
  internal pressure, material and insulation.

You can change radii, heights, pressures or material parameters here to
run your own scenarios.

---

### `boiloff_model.py`

Core analytical functions for a cryogenic tank:

- `tank_surface_area(radius, cyl_height)` – cylinder + 2 hemispherical domes.  
- `tank_volume(radius, cyl_height)` – matching volume model.  
- `shell_thickness(config)` – very simplified hoop-stress estimate.  
- `tank_shell_mass(config)` – shell mass from area × thickness × density.  
- `heat_leak(config)` – total heat leak \[W] from area × heat-leak density.  
- `boiloff_rate(config)` – boil-off rate \[kg/hour] from heat leak and latent heat.

The demo entry point:

```bash
python -m src.boiloff_model

prints a short summary, for example:

=== Cryogenic Tank Demo (LOX) ===
Shell mass:             XXXX.X kg
Heat leak:               XXX.X W
Boil-off rate:           X.XXX kg/hour
