---
name: machining-from-stock
description: Create conceptual machining stock, setup, and material-removal geometry around a target STEP using CadQuery.
---

# Machining From Stock

Use this skill when the user has a target part and wants to reason about stock size, machining setup, roughing envelope, or material removal.

## Required Inputs

- target STEP
- stock material and stock size
- setup orientation
- machine envelope
- fixture or vise assumptions
- tolerance or finish requirements

## Workflow

1. Import target STEP.
2. Measure target bounding box.
3. Create stock block or bar envelope.
4. Place target inside stock with machining allowance.
5. Create simplified fixture/vise geometry if needed.
6. Estimate removed volume as stock volume minus target volume.
7. Export stock, target, setup assembly, and report.

## CadQuery Outputs

- target reference
- stock block
- roughing envelope
- setup fixture concept
- machining setup assembly

## Validation Checks

- target fits inside stock
- minimum machining allowance is maintained
- setup orientation is documented
- removed volume is estimated
- fixture does not block critical machining access

