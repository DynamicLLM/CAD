---
name: progressive-die-cadquery
description: Use CadQuery and CQ-Editor to create conceptual progressive-die process geometry from a target part, material assumptions, and simple manufacturing rules.
---

# Progressive Die With CadQuery

Use this skill when the user wants to design, explain, or optimize conceptual progressive-die geometry using CadQuery, CQ-Editor, and STEP files.

## Scope

This skill is for conceptual and automation-oriented CAD geometry. It can generate and check:

- target part imports
- raw strip material
- station layout
- pilot holes
- piercing punches
- blanking punches
- lower die openings
- upper punch plates
- simplified die assembly
- STEP exports
- simple dimension, clearance, volume, and collision checks

It is not a replacement for NX Progressive Die Wizard, SolidWorks with 3DQuickPress/LogoPress, AutoForm, or a professional die designer.

## Required Inputs

Before generating tooling, collect or infer:

- target geometry, preferably STEP
- material
- sheet thickness
- quantity or production volume
- tolerance requirements
- preferred process: blanking, piercing, bending, forming, drawing, or progressive die
- strip direction
- minimum web/scrap bridge
- punch-to-die clearance
- station pitch
- press stroke/open height assumptions if making an assembly

If a value is unknown, choose a clearly labeled placeholder and keep it in a parameter block at the top of the script.

## Workflow

1. Import or define the target part.
2. Measure the target bounding box, thickness, volume, and major profiles.
3. Define material and process parameters at the top of the CadQuery script.
4. Create a raw strip or stock envelope.
5. Define stations along the feed direction.
6. Place pilot holes early in the strip if needed.
7. Place piercing operations before final blanking when possible.
8. Create upper punches from target openings or simplified envelopes.
9. Create lower die openings with clearance.
10. Create a simplified upper/lower assembly for visual inspection.
11. Export STEP files for each major object.
12. Verify bounding boxes, volumes, and object counts by re-importing the STEP files.
13. Display the objects in CQ-Editor with clear names.

## CadQuery Style

Use explicit parameters:

```python
MATERIAL = "mild steel"
SHEET_THICKNESS = 2.0
PUNCH_DIE_CLEARANCE_PER_SIDE = 0.08
STRIP_WIDTH = 50.0
STATION_PITCH = 80.0
```

Use `show_object` labels:

```python
show_object(target_part, name="01 target part")
show_object(raw_strip, name="02 raw strip")
show_object(lower_die, name="03 lower die")
show_object(upper_punches, name="04 upper punches")
show_object(assembly, name="05 process assembly")
```

Always export separate STEP files for review:

```python
cq.exporters.export(target_part, "01_target_part.step")
cq.exporters.export(raw_strip, "02_raw_strip.step")
cq.exporters.export(lower_die, "03_lower_die.step")
cq.exporters.export(upper_punches, "04_upper_punches.step")
cq.exporters.export(assembly, "05_process_assembly.step")
```

## Verification

For each exported STEP:

- re-import it with CadQuery
- report bounding box
- report volume when solid geometry is expected
- check that expected objects are not empty
- compare key dimensions with the source model

## References

Read the files in `references/` when planning:

- `input_checklist.md`
- `progressive_die_workflow.md`

