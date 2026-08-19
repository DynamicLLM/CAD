# Examples

This folder is reserved for CadQuery examples.

Planned examples:

- Simple pillow block from CadQuery Ex003
- Point-list hole placement from CadQuery Ex007
- `flat_blanking/flat_blanking_template.py`: target product, raw strip, lower die concept, pierce punches, blanking punch, and assembly.
- `fixture/fixture_template.py`: target reference, fixture base, locators, clamps, and fixture assembly.
- `machining/machining_from_stock_template.py`: target part, stock block, vise base concept, and machining setup assembly.

Run examples with a CadQuery-capable Python environment:

```powershell
python examples\flat_blanking\flat_blanking_template.py
python scripts\validate_step_files.py examples\flat_blanking\*.step
```
