---
name: cadquery-cad-foundation
description: Use CadQuery and CQ-Editor for general parametric CAD creation, STEP import/export, measurement, and display.
---

# CadQuery CAD Foundation

Use this skill when the task is general CAD automation rather than a specific manufacturing process.

## Scope

- Create simple parametric solids.
- Import STEP files.
- Measure bounding boxes, volume, area, solids, faces, and validity.
- Export STEP, STL, IGES where supported by the installed toolchain.
- Display generated objects in CQ-Editor with `show_object`.
- Prepare geometry for downstream case skills.

## Required Inputs

- target file path or desired geometry
- units, normally millimeters
- desired output formats
- viewer: CQ-Editor or FreeCAD

## Workflow

1. Read or create the geometry.
2. Put important dimensions in a parameter block.
3. Generate named CadQuery objects.
4. Export STEP files.
5. Re-import exported STEP files and report key measurements.
6. Open the script in CQ-Editor when visual inspection is requested.

## Output Pattern

```python
show_object(result, name="01 generated part")
cq.exporters.export(result, "01_generated_part.step")
```

## Verification

Always check:

- file exists
- STEP can be re-imported
- bounding box is plausible
- volume is nonzero for expected solid geometry

