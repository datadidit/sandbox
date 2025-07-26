# Hatch

## Installation

See installation instructions [here](https://hatch.pypa.io/latest/install/)

* My install example is below:

```bash
# Add virtual environment
Marcuss-MBP:hatch mkwyche$ python -m venv .venv
# Activate environment
Marcuss-MBP:hatch mkwyche$ . .venv/bin/activate
# Install hatch
pip install hatch
```

## Initialize Project

```bash
(.venv) Marcuss-MBP:hatch mkwyche$ hatch new --init
Project name: Hatch Demo
Description []: Demo project used to learn hatch

Wrote: pyproject.toml
```

This is useful but since I didn't do just `hatch new` it doesn't create the `src` directory and stuff for me it seems. So this route you'll need to update a bunch of stuff 
in the pyproject.toml manually. Still a pretty fleshed out start.

## TODOs

* Get pytest running with hatch
* Pytest logging to console w/ hatch and toml only no pytest.ini
* Understanding of pytest envs
