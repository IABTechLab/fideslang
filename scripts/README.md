## How To Use

First, setup your virtual environment and any dependencies:
```
python -m venv fides-venv
source fides-venv/bin/active
pip install -r dev-requirements.txt
```

## Generating JSON/CSV versions
The core taxonomy files are in YAML format, but for convenience it's sometimes useful to have JSON or CSV equivalents.

Use `python convert_yaml_format.py` to generate these files whenever a new version of the YAML is created.
