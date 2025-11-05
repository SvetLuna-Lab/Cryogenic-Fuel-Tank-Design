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


compare_materials.py

Compares two material options for the same geometry and insulation:

baseline Al–Li 2195 tank,

conceptual CFRP + liner tank.

For each configuration it computes:

shell mass [kg],

boil-off rate [kg/hour].

Run:

python -m src.compare_materials


Example output:

=== Material comparison (same geometry) ===
Al-Li 2195               shell mass =   XXXX.X kg, boil-off = X.XXX kg/h
CFRP tank (concept)      shell mass =   YYYY.Y kg, boil-off = Y.YYY kg/h

Note: CFRP mass is lower, but real designs require liner, complex QA and
qualification, and have higher technical risk.


This mirrors typical trade-offs in cryogenic tank design: mass vs
technology readiness vs risk.

Usage notes

All scripts assume SI units (metres, kilograms, Pascals, Watts).

The numbers are order-of-magnitude and intended for didactic
purposes, not for detailed sizing.

For more serious work, each assumption (heat-leak density, stress
limits, safety factors) should be backed by test data or standards.

You can extend this folder with:

Jupyter notebooks for parameter sweeps,

additional material options and load cases,

simple plotting utilities based on matplotlib.
