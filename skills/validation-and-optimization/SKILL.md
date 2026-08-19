---
name: validation-and-optimization
description: Validate and compare CadQuery-generated CAD/process variants using STEP re-imports, dimensions, volume, material use, clearance, force, and collision checks.
---

# Validation And Optimization

Use this skill after geometry has been generated or when the user asks Codex to optimize a CAD/manufacturing concept.

## Inputs

- generated STEP files
- parameter values used to create them
- target dimensions
- material data
- objective function
- constraints

## Common Objectives

- minimize material usage
- minimize number of stations
- minimize removed machining volume
- balance press force
- keep geometry within stock or machine envelope
- avoid collisions
- preserve target dimensions

## Workflow

1. Re-import every exported STEP.
2. Measure bounding boxes and volumes.
3. Compare target dimensions with baseline dimensions.
4. Compute process metrics such as utilization, removed volume, or approximate force.
5. Check constraints and report pass/fail.
6. Generate a ranked table of variants.
7. Recommend the next parameter change.

## Progressive-Die Metrics

```text
material_utilization = parts_per_pitch * part_area / (station_pitch * strip_width)
blanking_force = cut_perimeter * sheet_thickness * shear_strength
force_moment = sum(force_i * x_i)
```

## Output

- concise validation report
- variant comparison table
- recommended next iteration
- list of assumptions that need engineering confirmation

