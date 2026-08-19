---
name: fixture-design
description: Design conceptual fixtures for locating, supporting, and clamping a target part using CadQuery geometry and STEP inspection.
---

# Fixture Design

Use this skill when the user wants a fixture, jig, locator, or workholding concept for an existing target STEP or generated part.

## Required Inputs

- target STEP
- operation: inspection, machining, welding, assembly, drilling, or forming
- datum surfaces
- clamp directions
- clearance requirements
- stock or machine envelope

## Workflow

1. Import target STEP.
2. Measure bounding box and identify likely datum faces.
3. Define base plate, rest pads, side locators, end stops, and clamps.
4. Keep all fixture parameters at the top of the script.
5. Check access to required machining or inspection faces.
6. Export target, fixture, and assembly STEP files.
7. Display the assembly in CQ-Editor.

## CadQuery Outputs

- target reference
- fixture base plate
- locators/rest pads
- clamp blocks
- fixture assembly

## Validation Checks

- target is not modified
- fixture does not collide with protected part areas
- clamps are placed on reasonable support zones
- datum/locator assumptions are reported
- tool access is checked conceptually

