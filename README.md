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

skills/
  progressive-die-cadquery/
    SKILL.md
    references/
      progressive_die_workflow.md
      input_checklist.md

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

