## How To Use

From the root directory of this repo, setup a virtual environment and install `fideslang` locally:
```
python -m venv venv
source venv/bin/activate
pip install .
```

## Generating JSON/CSV/YAML files from the Taxonomy
The core taxonomy files are in YAML format, but for convenience it's sometimes useful to have JSON or CSV equivalents.

Use `python scripts/export_default_taxonomy.py` to generate these files whenever a new version of the YAML is created.