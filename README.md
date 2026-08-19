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
| `cadquery-cad-foundation` | The task is general STEP/CadQuery creation, import, export, measurement, or CQ-Editor viewing. |
| `progressive-die-cadquery` | The task needs the parent progressive-die workflow or an NX-inspired overview. |
| `progressive-die-flat-blanking` | The part is mostly flat sheet metal and needs piercing, trimming, strip layout, and blanking. |
| `progressive-die-bending` | The part has flanges, tabs, simple bends, bend allowance, or springback assumptions. |
| `progressive-die-drawing-forming` | The part has draw, emboss, rib, or freeform sheet-metal forming features. |
| `fixture-design` | The task is locating, clamping, holding, or supporting a target part. |
| `machining-from-stock` | The task starts with stock material and a target shape, then reasons about setup and removal. |
| `validation-and-optimization` | The task compares variants or checks dimensions, material use, force, clearance, or collisions. |
