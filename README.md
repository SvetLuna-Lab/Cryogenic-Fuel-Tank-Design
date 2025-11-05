# Cryogenic Fuel Tank Design — Launch Vehicle Study  

**Author:** S. I. Romanova  
**Year:** 2025  

---

## Overview  

This repository documents a **conceptual structural design** for a cryogenic fuel tank used in space launch vehicles.  
The focus is on linking **engineering requirements** (thermal, structural, safety) with a small, transparent **Python model**.

Key aspects:

- **Thermal insulation**  
  - Multilayer insulation (MLI) + vacuum jacket  
  - Minimising thermal bridges through supports and interfaces  

- **Material selection**  
  - Aluminum–lithium (Al–Li) cryogenic tank as baseline  
  - Composite (CFRP + liner) tank as a mass-saving, higher-risk option  

- **Safety & boil-off control**  
  - Acceptable boil-off rates for LOX / LH₂  
  - Over-pressure protection and vent logic  

The code in `src/` is intentionally simple: it is not a flight design, but an **educational, reproducible** example.

---

## Repository structure  

(Current state; some folders are planned.)

- `src/`
  - `tank_config.py` – baseline configuration: geometry, materials, insulation parameters.  
  - `boiloff_model.py` – simple heat-leak and boil-off estimation for LOX / LH₂ tanks.  
  - `compare_materials.py` – mass and qualitative risk comparison of Al–Li vs composite tanks.  

- `requirements.txt` – Python dependencies (minimal: `numpy`, optionally `matplotlib` if you add plots).  

**Planned (not yet in the repo, but referenced in the design):**

- `report/CryoTank_Design_Romanova_SI.pdf` – main engineering brief (requirements, diagrams, tables).  
- `figures/` – schematic cross-sections, insulation stack-ups, material trade-off table.  
- `docs/` – markdown chapters (intro, material selection, insulation & boil-off, safety & tests, references).

---

## Quick start — Python model  

### 1. Create environment and install dependencies  

```bash
# (optional) create a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

pip install -r requirements.txt


2. Estimate boil-off for a baseline Al–Li tank
python -m src.boiloff_model

The script prints an approximate heat leak (W) and boil-off rate (kg/hour) for a reference LOX or LH₂ tank, using the configuration from tank_config.py.


3. Compare Al–Li vs composite tank mass
python -m src.compare_materials


The script reports, for each material option:

shell mass estimate,

hoop-stress safety margin,

qualitative notes on technology readiness and risk (permeation, NDI/repair, cost).

You can adjust parameters such as diameter, wall thickness, design pressure, and material properties directly in tank_config.py.


Engineering context (short abstract)

The tank is sized for LOX / LH₂ storage in an upper or booster stage with long pre-launch dwell time and repeated cryogenic cycles.

Thermal insulation

Vacuum jacket with ~30–40 MLI layers and, where needed, spray-on foam insulation (SOFI).

Support struts made of GFRP/CFRP with thermal breaks to reduce conduction.

Material selection

Baseline: welded Al–Li alloy tank (e.g. 2195) with orthogrid stiffening, high TRL and well-documented cryogenic behaviour.

Alternative: CFRP + metallic liner, ~20–30 % lighter but with higher risk in terms of permeation, inspection, and qualification costs.

Boil-off & pressurisation

Target heat leak: 2–5 W/m² for LH₂, 5–10 W/m² for LOX.

Boil-off gas routed to autogenous pressurisation, RCS, or safe venting.

Redundant relief valves (2oo3 logic) and continuous monitoring of pressure, temperature and level.

This study is educational and does not represent a certified flight design.
It is meant as a clear example of how structural, thermal, and safety considerations can be turned into simple analytical tools.


Roadmap

Planned improvements:

Add the full engineering PDF brief to report/.

Upload schematic figures (tank geometry, insulation stack-up, material trade-off table).

Extend boiloff_model.py with separate LOX/LH₂ presets and plotting utilities.

Provide Jupyter notebooks for parameter sweeps and sensitivity studies.


Citation

If you reference this work in reports or coursework, you can cite it as:

Romanova, S. I. (2025). Cryogenic Fuel Tank Design — Structural, Thermal, and Safety Considerations for Launch Vehicles.
GitHub repository:

License

Specify license here (e.g. MIT, Apache-2.0) once chosen.

