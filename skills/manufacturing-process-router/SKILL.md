---
name: manufacturing-process-router
description: Choose the correct CAD/manufacturing skill case before creating or modifying CadQuery, STEP, fixture, die, machining, or optimization files.
---

# Manufacturing Process Router

Use this skill first when a user asks for a manufacturing-process concept and the correct case is not already explicit.

## Routing Questions

Classify the request by asking what the target represents:

- A geometry-only CAD task: use `cadquery-cad-foundation`.
- A flat sheet-metal part cut from strip: use `progressive-die-flat-blanking`.
- A sheet-metal part with bends/flanges/tabs: use `progressive-die-bending`.
- A drawn, embossed, ribbed, or freeform sheet-metal part: use `progressive-die-drawing-forming`.
- A tool to hold or locate a part: use `fixture-design`.
- A target shape made from block/bar/plate stock: use `machining-from-stock`.
- A comparison or parameter search: use `validation-and-optimization` after the generator skill.

## Default Assumptions

If the user provides only a STEP file:

1. Inspect the STEP geometry first.
2. If it is thin and mostly planar, choose flat blanking.
3. If it has obvious bends or flanges, choose bending.
4. If it has deep/freeform deformation, choose drawing/forming and mark the output conceptual.
5. If it is not sheet metal, ask whether the process is machining, fixture design, casting, molding, or another process.

## Required Output

Always state:

- selected skill case
- reason for the selection
- missing inputs
- assumptions used to proceed
- expected files to generate

