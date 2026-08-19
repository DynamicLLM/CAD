---
name: progressive-die-drawing-forming
description: Create early-stage conceptual geometry for drawn, embossed, or freeform sheet-metal progressive-die processes using CadQuery placeholders and explicit assumptions.
---

# Progressive Die Drawing And Forming

Use this skill when the target has drawn cups, embosses, ribs, freeform forms, or significant material flow.

## Required Inputs

- target STEP
- material, thickness, and formability assumptions
- draw depth
- corner radii
- blank holder or binder assumptions
- number of forming stages
- allowable thinning or strain criteria, if known

## Workflow

1. Import target STEP and identify forming regions.
2. Separate simple piercing/blanking operations from forming operations.
3. Create simplified intermediate stages rather than pretending to solve true forming physics.
4. Create placeholder forming punches/dies using envelopes and offsets.
5. Mark all unvalidated forming geometry as conceptual.
6. Export staged geometry and a limitations report.

## CadQuery Outputs

- target part
- approximate developed blank
- intermediate forming stages
- forming punch envelope
- lower forming die envelope
- conceptual assembly

## Validation Checks

- draw depth and radius assumptions documented
- sharp forming regions flagged
- holes/features near forming regions flagged
- station sequence separates forming, trimming, and final cutoff
- limitations clearly reported

## Boundary

Real drawing/forming requires forming simulation or expert validation. CadQuery can help organize geometry, but it cannot replace AutoForm, NX forming analysis, or physical tryout data.

