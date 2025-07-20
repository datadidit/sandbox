# PyProject

Need to get a better understanding of pyproject.toml

## Notes

* Bare bones it appears the dependencies won't install without a `build backend` so you're not supposed to use the **pyproject.toml** directly with pip. 
Example can be seen [here](barebones_pyproject.toml). Error I get is below:

```bash
      ValueError: Unable to determine which files to ship inside the wheel using the following heuristics: https://hatch.pypa.io/latest/plugins/builder/wheel/#default-file-selection

      The most likely cause of this is that there is no directory that matches the name of your project (hello_pyproject).

      At least one file selection option must be defined in the `tool.hatch.build.targets.wheel` table, see: https://hatch.pypa.io/latest/config/build/

      As an example, if you intend to ship a directory named `foo` that resides within a `src` directory located at the root of your project, you can define the following:

      [tool.hatch.build.targets.wheel]
      packages = ["src/foo"]
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
```
* Once the necessary files were in place for the backend the build worked:

```
(.venv) Marcuss-MBP:pyproject mkwyche$ pip install .
Processing /Users/mkwyche/workspace/sandbox/python/pyproject
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: pydantic in ./.venv/lib/python3.13/site-packages (from hello_pyproject==0.0.1) (2.11.7)
Collecting sqlalchemy (from hello_pyproject==0.0.1)
  Downloading sqlalchemy-2.0.41-cp313-cp313-macosx_10_13_x86_64.whl.metadata (9.6 kB)
Requirement already satisfied: annotated-types>=0.6.0 in ./.venv/lib/python3.13/site-packages (from pydantic->hello_pyproject==0.0.1) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in ./.venv/lib/python3.13/site-packages (from pydantic->hello_pyproject==0.0.1) (2.33.2)
Requirement already satisfied: typing-extensions>=4.12.2 in ./.venv/lib/python3.13/site-packages (from pydantic->hello_pyproject==0.0.1) (4.14.1)
Requirement already satisfied: typing-inspection>=0.4.0 in ./.venv/lib/python3.13/site-packages (from pydantic->hello_pyproject==0.0.1) (0.4.1)
Collecting greenlet>=1 (from sqlalchemy->hello_pyproject==0.0.1)
  Downloading greenlet-3.2.3-cp313-cp313-macosx_11_0_universal2.whl.metadata (4.1 kB)
Downloading sqlalchemy-2.0.41-cp313-cp313-macosx_10_13_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 3.4 MB/s eta 0:00:00
Downloading greenlet-3.2.3-cp313-cp313-macosx_11_0_universal2.whl (270 kB)
Building wheels for collected packages: hello_pyproject
  Building wheel for hello_pyproject (pyproject.toml) ... done
  Created wheel for hello_pyproject: filename=hello_pyproject-0.0.1-py2.py3-none-any.whl size=2008 sha256=662361f583bdceef575a541bb1706443e0dfb8a374f37dc80b25093d0aa2e32d
  Stored in directory: /private/var/folders/ns/rnz3jkj11073ghczyknpvp800000gn/T/pip-ephem-wheel-cache-8vgbn20e/wheels/a4/f4/cd/1f2c3d35f222b09cbb1b09a4ad76f63aeb945b092529f72119
Successfully built hello_pyproject
Installing collected packages: greenlet, sqlalchemy, hello_pyproject
  Attempting uninstall: hello_pyproject
    Found existing installation: hello_pyproject 0.0.1
    Uninstalling hello_pyproject-0.0.1:
      Successfully uninstalled hello_pyproject-0.0.1
Successfully installed greenlet-3.2.3 hello_pyproject-0.0.1 sqlalchemy-2.0.41
```

## Important Terms

* [Build Backend](https://packaging.python.org/en/latest/glossary/#term-Build-Backend): A library that takes a source tree and builds a source distribution from it. Note this is different than a Build Backend(e.g. pip)
* [Build Frontend](https://packaging.python.org/en/latest/glossary/#term-Build-Frontend)
* [Wheel](https://packaging.python.org/en/latest/glossary/#term-Wheel)

## VSCode

* Ensure the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) is installed. 
