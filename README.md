# Cryogenic Fuel Tank Design — Launch Vehicle Study

Author: S. I. Romanova  
Year: 2025  

This repository documents a conceptual structural design for a **cryogenic fuel tank** used in space launch vehicles.  
The focus is on:

- thermal insulation (MLI + vacuum jacket, minimising thermal bridges),
- material selection (Al–Li alloys versus composite tanks),
- safety measures against **boil-off losses** and over-pressure.

The project combines an engineering report (PDF) and a small, reproducible Python model that estimates tank mass and propellant boil-off for simple load cases.

---

## Repository structure

- `report/CryoTank_Design_Romanova_SI.pdf` — main design document (geometry, loads, safety, references).
- `figures/` — schematic figures (tank cross-section, insulation stack, support struts).
- `src/tank_config.py` — data structures describing tank geometry, material, and insulation.
- `src/boiloff_model.py` — simple heat-leak and boil-off estimation model.
- `src/compare_materials.py` — comparison of Al–Li and composite designs.
- `data/sample_loadcase.json` — example input (pressure, temperature, dwell time).
- `requirements.txt` — Python dependencies (NumPy, matplotlib if plots are added).

---

## Quick start (Python model)

Create and activate a virtual environment (optional), then install dependencies:

```bash
pip install -r requirements.txt


1. Estimate boil-off for a baseline Al–Li tank
python -m src.boiloff_model


This will print an approximate heat leak [W] and boil-off rate [kg/hour] for a reference LOX or LH₂ tank

2. Compare Al–Li vs composite tank mass
python -m src.compare_materials


The script reports:

shell mass for each material,

safety margin on hoop stress,

qualitative notes on risk / technology readiness.


Engineering context (short abstract)

The tank is intended for LOX / LH₂ storage in a launch-vehicle stage with long pre-launch dwell time and multiple cryogenic cycles.

Thermal insulation: multilayer insulation (MLI) with aluminised reflective foils and low-conductivity spacers, enclosed in a vacuum jacket. Support struts and flanges are designed to minimise thermal bridges through the use of GFRP/CFRP and thermal breaks.

Material selection: a welded Al–Li alloy tank (e.g. 2195) is used as baseline due to high TRL, good cryogenic toughness, and well-understood weld behaviour. Composite tanks (CFRP with liner) are considered as a mass-saving but higher-risk option.

Boil-off control: gas management system routes vapour to attitude-control / pressurisation or to safe venting. Redundant relief valves and continuous temperature/pressure monitoring ensure safety.

This repository is educational and does not represent a certified flight design. It is meant as a transparent, reproducible example of how structural, thermal, and safety considerations can be linked with simple analytical models.

Citation

Romanova, S. I. (2025). Cryogenic Fuel Tank Design — Structural, Thermal, and Safety Considerations for Launch Vehicles.
GitHub repository: <add-repo-url-here>.


















