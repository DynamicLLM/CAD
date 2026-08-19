---
name: progressive-die-bending
description: Plan conceptual progressive-die station geometry for bent sheet-metal parts using CadQuery, with bend allowance and springback assumptions exposed as parameters.
---

# Progressive Die Bending

Use this skill when a sheet-metal part has bends, flanges, tabs, or simple formed angles.

## Required Inputs

- final bent target geometry or sketch
- material and sheet thickness
- bend radius
- bend angle
- K-factor or bend allowance assumption
- springback assumption
- grain direction if relevant
- station sequence

## Workflow

1. Measure final part geometry.
2. Define flat blank assumptions using bend allowance.
3. Create staged shapes: flat blank, pre-bend, overbend, final bend.
4. Define forming stations after piercing/trimming where practical.
5. Generate simplified lower forming die and upper forming punch geometry.
6. Include springback/overbend parameters at the top of the script.
7. Display stages in CQ-Editor as separate named objects.

## CadQuery Outputs

- flat blank concept
- staged intermediate parts
- forming punch concept
- lower forming die concept
- assembly STEP

## Validation Checks

- developed blank length is documented
- bend radius is not below assumed minimum
- forming stations do not collide with previous features
- holes close to bend lines are flagged
- springback assumption is visible in the report

## Limitations

CadQuery can create the geometry, but it does not simulate plastic deformation, thinning, strain, or springback physics. Use this as a planning geometry workflow, not as forming simulation.

