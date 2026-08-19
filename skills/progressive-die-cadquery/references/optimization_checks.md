# Optimization Checks

Use this checklist when Codex is asked to optimize a progressive-die concept.

## Geometry Checks

- Target part bounding box unchanged.
- Target part thickness matches material thickness or stated assumption.
- Raw strip fully covers each station profile.
- Upper punches align with lower die openings.
- Clearance is positive and documented.
- Final blanking happens after internal piercing unless the user asks otherwise.

## Material Use

- Estimate strip width.
- Estimate station pitch.
- Estimate part area.
- Compute material utilization.
- Compare variants by utilization and scrap width.

## Force And Balance

For rough blanking force:

```text
force = cut_perimeter * sheet_thickness * shear_strength
```

For balance:

```text
moment = sum(force_i * station_or_feature_x_i)
```

These estimates are screening tools only. Real die design needs validated material data and press/tooling standards.

## Manufacturability

- Avoid thin, fragile lower die walls.
- Keep minimum distance between nearby holes or openings.
- Leave enough stock around guide pins and screws.
- Avoid very tall/slender punches without support.
- Add reliefs where slugs or formed material need escape.

## Variant Report

For each variant, save:

- parameter values
- output STEP file names
- bounding boxes
- volume/area when available
- utilization estimate
- force estimate
- main tradeoff
