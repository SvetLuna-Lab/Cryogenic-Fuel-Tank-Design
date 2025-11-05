# Cryogenic Fuel Tank Design — Launch Vehicle Study  

**Author:** S. I. Romanova  
**Year:** 2025  

---

## Overview  

This repository documents a **conceptual design** of a cryogenic fuel tank for space launch vehicles.  
The goal is to connect engineering requirements (thermal, structural, safety) with a small, transparent  
**Python model** for boil-off and material trade-off.

Key focus areas:

- **Thermal insulation**  
  Multilayer insulation (MLI) + vacuum jacket, with minimised thermal bridges in supports and interfaces.

- **Material selection**  
  Baseline: welded Al–Li cryogenic tank.  
  Alternative: CFRP + liner concept with lower mass but higher technical risk.

- **Boil-off & safety**  
  Acceptable boil-off rates for LOX / LH₂, over-pressure protection, and simple analytical estimates.

This is an **educational** repository. It does not represent a certified flight design, but demonstrates  
how structural, thermal, and safety considerations can be turned into reproducible code.

---

## Repository structure  

```text
.
├── src/
│   ├── tank_config.py         # Baseline geometry, material, insulation parameters
│   ├── boiloff_model.py       # Heat-leak and boil-off estimation for LOX / LH₂
│   ├── compare_materials.py   # Al–Li vs CFRP mass and risk comparison
│   └── README.md              # Description of the Python model
├── report/
│   ├── Cryogenic_Fuel_Tank_Design_Romanova_SI.pdf      # 1-page concept brief
│   └── PDR_Draft_Svetlana_Romanova_Final.pdf           # Extended PDR-style document
├── figures/
│   ├── requirements_table.png          # Key thermal/pressure/boil-off requirements   (optional)
│   ├── tank_schematic.png              # LOX/LH₂ tank with common bulkhead           (optional)
│   └── material_tradeoff.png           # Al–Li vs CFRP + liner trade-off             (optional)
├── data/
│   └── sample_loadcase.json            # Example load case (pressure, dwell, temps)
├── requirements.txt                    # Python dependencies (NumPy, Matplotlib)
└── LICENSE                             # Project license (e.g. MIT)


If some images in figures/ are not yet present, they are intended as
placeholders for exported diagrams from the PDF reports.


Quick start (Python model)
1. Install dependencies

# (optional) create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

pip install -r requirements.txt


2. Estimate boil-off for the baseline tank

python -m src.boiloff_model


Example console output:

=== Cryogenic Tank Demo (LOX) ===
Shell mass:             XXXX.X kg
Heat leak:               XXX.X W
Boil-off rate:           X.XXX kg/hour


3. Compare Al–Li vs CFRP

python -m src.compare_materials

Example console output:

=== Material comparison (same geometry) ===
Al-Li 2195               shell mass =   XXXX.X kg, boil-off = X.XXX kg/h
CFRP tank (concept)      shell mass =   YYYY.Y kg, boil-off = Y.YYY kg/h

Note: CFRP mass is lower, but real designs require liner, complex QA and
qualification, and have higher technical risk.

You can modify src/tank_config.py to explore other radii, heights, pressures and materials.


Reports

The main engineering description is provided as PDF:

report/Cryogenic_Fuel_Tank_Design_Romanova_SI.pdf
– one-page concept summary (requirements, insulation strategy, material trade-off).

Optional extended document:

report/PDR_Draft_Svetlana_Romanova_Final.pdf
– preliminary design review with mission context, engine+tank schematic, and risk/test considerations.


Status & roadmap

Current:

Basic analytical model for shell mass and boil-off.

Simple material comparison between Al–Li and CFRP + liner.

Design brief and PDR-style document in report/.

Planned (optional enhancements):

Export schematic figures from the PDFs into figures/ and reference them from README/docs.

Add notebooks for parameter sweeps and sensitivity studies.

Refine input data in data/sample_loadcase.json for multiple scenarios.


Citation

If you reference this work in reports or coursework:

Romanova, S. I. (2025). Cryogenic Fuel Tank Design — Structural, Thermal, and Safety Considerations for Launch Vehicles. GitHub repository.


License

The project is released under the terms of the license specified in LICENSE
(for example, MIT).
Please check that file before reuse.




