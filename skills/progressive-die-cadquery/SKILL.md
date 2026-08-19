---
name: progressive-die-cadquery
description: Use CadQuery and CQ-Editor to create conceptual progressive-die process geometry from a target part, material assumptions, and simple manufacturing rules.
---

# Progressive Die With CadQuery

Use this skill when the user wants to design, explain, or optimize conceptual progressive-die geometry using CadQuery, CQ-Editor, and STEP files.

This skill is inspired by public descriptions of NX Progressive Die Wizard workflows. It paraphrases public workflow concepts and converts them into an open CadQuery process. Do not copy Siemens, NX, or third-party proprietary manuals into this skill.

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

## Source Policy

Use public sources only for high-level workflow understanding:

- product capability pages
- public course outlines
- public command indexes
- public engineering articles
- open research papers

Write the final workflow in original language. Include source links in reports, but do not paste long source text or copyrighted training procedures.

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

## NX-Inspired Workflow Map

Translate commercial progressive-die workflow concepts into the following open process:

| NX-style concept | CadQuery/CQ-Editor equivalent |
| --- | --- |
| Part preparation | Import target STEP, measure thickness, detect solids/faces |
| Blank generator | Derive flat blank/profile or use target outline as placeholder |
| Blank layout | Create one-row or multi-row blank arrangement on strip |
| Scrap design | Define edge web, scrap bridge, carrier, slug removal zones |
| Strip layout | Place stations along feed direction and show staged strip |
| Die base management | Generate simplified lower/upper plates and spacing |
| Standard parts | Parameterized guide pins, screws, dowels, springs as simplified solids |
| Piercing/forming inserts | Generate punches and lower die openings from profiles |
| Force calculation | Estimate blanking/piercing force from perimeter, thickness, shear strength |
| Validation | Check clearances, bounding boxes, collisions, material utilization |
| Drawings | Export STEP and optionally create notes/tables outside CadQuery |

## Geometry Workflow

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

## Optimization Loop

For optimization tasks, define objective functions before changing geometry:

- minimize number of stations
- improve material utilization
- balance press force or center of pressure
- maintain minimum scrap bridge and edge web
- maintain punch/die clearance
- avoid collisions between punches, plates, and strip
- keep tooling manufacturable with simple pockets and reliefs

Generate variants by changing parameter blocks, not by hard-coding geometry edits. Save each variant with a versioned folder name and a short assumptions file.

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
