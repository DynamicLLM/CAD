# CAD

Private working repository for AI-assisted CAD automation experiments.

The initial focus is:

- Python installation for CAD scripting
- CadQuery installation and STEP generation
- CQ-Editor visualization workflow
- FreeCAD as an optional STEP inspection and translation tool
- A progressive-die design assistant skill inspired by public NX progressive die workflow descriptions

This repository is intentionally practical. It does not try to replace NX, SolidWorks, 3DQuickPress, or LogoPress. Instead, it captures a programmable workflow where Codex writes or modifies CadQuery scripts, CadQuery generates geometry, and CQ-Editor displays the result.

## Repository Structure

```text
docs/
  installation.md
  public_sources.md
  NX_Public_Progressive_Die_Workflow_Reorganized.docx

skills/
  manufacturing-process-router/
  cadquery-cad-foundation/
  progressive-die-flat-blanking/
  progressive-die-bending/
  progressive-die-drawing-forming/
  progressive-die-cadquery/
  fixture-design/
  machining-from-stock/
  validation-and-optimization/
    SKILL.md
    references/

examples/
  README.md
  flat_blanking/
  fixture/
  machining/

shared/
  materials/
  formulas/
  cadquery_patterns/
  report_templates/

scripts/
  validate_step_files.py
```

## Core Workflow

```text
engineering requirement / target STEP / material data
        ↓
Codex applies the progressive-die CadQuery skill
        ↓
CadQuery script generates process geometry
        ↓
CQ-Editor displays final part, strip, punches, dies, and assembly
        ↓
STEP files are exported
        ↓
dimensions, material use, clearances, and simple collisions are checked
        ↓
iterate parameters or process sequence
```

## Important Boundary

CadQuery and FreeCAD can create and inspect geometry, but they do not automatically contain industrial progressive-die manufacturing knowledge. The process rules in this repository must be supplied by engineering references, company standards, or explicit user assumptions.

## Skill Cases

| Skill | Use when |
| --- | --- |
| `manufacturing-process-router` | The process is unclear and Codex should choose the correct case skill first. |
| `cadquery-cad-foundation` | The task is general STEP/CadQuery creation, import, export, measurement, or CQ-Editor viewing. |
| `progressive-die-cadquery` | The task needs the parent progressive-die workflow or an NX-inspired overview. |
| `progressive-die-flat-blanking` | The part is mostly flat sheet metal and needs piercing, trimming, strip layout, and blanking. |
| `progressive-die-bending` | The part has flanges, tabs, simple bends, bend allowance, or springback assumptions. |
| `progressive-die-drawing-forming` | The part has draw, emboss, rib, or freeform sheet-metal forming features. |
| `fixture-design` | The task is locating, clamping, holding, or supporting a target part. |
| `machining-from-stock` | The task starts with stock material and a target shape, then reasons about setup and removal. |
| `validation-and-optimization` | The task compares variants or checks dimensions, material use, force, clearance, or collisions. |

## Foundation Expansion

The repository now has a reusable foundation layer:

- `shared/materials/` contains placeholder material notes.
- `shared/formulas/` contains screening formulas for utilization, force, and stock removal.
- `shared/cadquery_patterns/` contains reusable script patterns.
- `shared/report_templates/` contains concept-report structure.
- `scripts/validate_step_files.py` re-imports STEP files and reports dimensions, volume, area, and validity.

Examples are intentionally simple. They exist to prove the workflow:

```text
skill case
        ↓
CadQuery template
        ↓
STEP files
        ↓
validation script
        ↓
CQ-Editor display
```
