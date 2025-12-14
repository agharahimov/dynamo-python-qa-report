# Dynamo + Python QA Report (Portable Prototype)

This repository demonstrates a **portable Python workflow** intended for **Dynamo Python nodes** used in Revit BIM automation.

Because Revit/Dynamo require Windows, this project uses **mock Revit-like element data** (JSON) to implement and test:
- parameter extraction
- QA/QC validation checks
- report generation (CSV / JSON + summary)

This approach allows development and demonstration of automation logic on **macOS**, with seamless future integration into **Dynamo + Revit** environments.

---

## Project Goals

- Simulate Revit element parameter access
- Apply QA/QC and compliance-style validation rules
- Generate structured reports used in BIM documentation workflows
- Keep the code **Dynamo-ready** and **platform-independent**

---

## Repository Structure

```
dynamo-python-qa-report/
├── data/
│   └── sample_elements.json
├── reports/
│   └── .gitkeep
├── src/
│   └── dynamo_qa/
│       ├── cli.py
│       ├── core/
│       ├── io/
│       └── qa/
├── tests/
├── pyproject.toml
└── README.md
```

---

## How to Run

From the repository root:

```bash
PYTHONPATH=src python -m dynamo_qa.cli
```

Optional arguments:

```bash
python -m dynamo_qa.cli --input data/sample_elements.json --outdir reports
```

---

## Outputs

Running the script generates:

- `reports/report.csv` — flat table with extracted parameters and issue counts
- `reports/report.json` — full structured output with per-element issues
- `reports/summary.txt` — overview of total elements and QA issue statistics

---

## Running Tests

```bash
PYTHONPATH=src pytest -q
```

---

## Dynamo / Revit Integration Concept

In Dynamo, a Python node typically receives Revit elements via `IN[0]`.

To integrate this logic:
1. Replace JSON loading with Revit element input
2. Map Revit parameters to the `Element` data model
3. Use the same QA and reporting logic without modification

This mirrors real-world BIM automation workflows such as:
- documentation validation
- parameter compliance checks
- automated QA/QC reporting