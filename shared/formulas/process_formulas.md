# Process Formulas

These formulas are early screening estimates, not certified manufacturing calculations.

## Material Utilization

```text
material_utilization = parts_per_pitch * part_area / (station_pitch * strip_width)
```

## Blanking Or Piercing Force

```text
cutting_force = cut_perimeter * sheet_thickness * shear_strength
```

## Approximate Removed Machining Volume

```text
removed_volume = stock_volume - target_volume
```

## Simple Force Moment

```text
force_moment_x = sum(force_i * x_i)
```

Use this to compare alternatives, not to approve a production die.

