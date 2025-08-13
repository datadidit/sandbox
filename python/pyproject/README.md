# PyProject

Need to get a better understanding of pyproject.toml

## Commands

* Setup virtualenv

```
python -m venv .venv
```

* Activate virtualenv

```
macbookpro:pyproject mkwyche$ . .venv/bin/activate
(.venv) macbookpro:pyproject mkwyche$
```

Note nothing currently in your virtualenv

```
macbookpro:pyproject mkwyche$ ls -l .venv/lib/python3.13/site-packages/
total 0
drwxr-xr-x   9 mkwyche  staff  288 Aug 13 02:30 pip
drwxr-xr-x  10 mkwyche  staff  320 Aug 13 02:30 pip-25.1.1.dist-info
```

* Use pip to install dependencies from your `toml` into your environment

```
macbookpro:pyproject mkwyche$ pip install .
Processing /Users/mkwyche/workspace/sandbox/python/pyproject
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pydantic (from hello_pyproject==0.0.1)
  Using cached pydantic-2.11.7-py3-none-any.whl.metadata (67 kB)
Collecting sqlalchemy (from hello_pyproject==0.0.1)
  Using cached sqlalchemy-2.0.43-cp313-cp313-macosx_10_13_x86_64.whl.metadata (9.6 kB)
Collecting annotated-types>=0.6.0 (from pydantic->hello_pyproject==0.0.1)
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.33.2 (from pydantic->hello_pyproject==0.0.1)
  Using cached pydantic_core-2.33.2-cp313-cp313-macosx_10_12_x86_64.whl.metadata (6.8 kB)
Collecting typing-extensions>=4.12.2 (from pydantic->hello_pyproject==0.0.1)
  Using cached typing_extensions-4.14.1-py3-none-any.whl.metadata (3.0 kB)
Collecting typing-inspection>=0.4.0 (from pydantic->hello_pyproject==0.0.1)
  Using cached typing_inspection-0.4.1-py3-none-any.whl.metadata (2.6 kB)
Collecting greenlet>=1 (from sqlalchemy->hello_pyproject==0.0.1)
  Using cached greenlet-3.2.4-cp313-cp313-macosx_11_0_universal2.whl.metadata (4.1 kB)
Using cached pydantic-2.11.7-py3-none-any.whl (444 kB)
Using cached pydantic_core-2.33.2-cp313-cp313-macosx_10_12_x86_64.whl (2.0 MB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached typing_extensions-4.14.1-py3-none-any.whl (43 kB)
Using cached typing_inspection-0.4.1-py3-none-any.whl (14 kB)
Using cached sqlalchemy-2.0.43-cp313-cp313-macosx_10_13_x86_64.whl (2.1 MB)
Using cached greenlet-3.2.4-cp313-cp313-macosx_11_0_universal2.whl (272 kB)
Building wheels for collected packages: hello_pyproject
  Building wheel for hello_pyproject (pyproject.toml) ... done
  Created wheel for hello_pyproject: filename=hello_pyproject-0.0.1-py2.py3-none-any.whl size=2995 sha256=b03a4a737ac891d065e84035bbe3e7d66aeaa18260de1288a9d881ce96d5abc1
  Stored in directory: /private/var/folders/ns/rnz3jkj11073ghczyknpvp800000gn/T/pip-ephem-wheel-cache-fbbr2uvb/wheels/a4/f4/cd/1f2c3d35f222b09cbb1b09a4ad76f63aeb945b092529f72119
Successfully built hello_pyproject
Installing collected packages: typing-extensions, greenlet, annotated-types, typing-inspection, sqlalchemy, pydantic-core, pydantic, hello_pyproject
Successfully installed annotated-types-0.7.0 greenlet-3.2.4 hello_pyproject-0.0.1 pydantic-2.11.7 pydantic-core-2.33.2 sqlalchemy-2.0.43 typing-extensions-4.14.1 typing-inspection-0.4.1

[notice] A new release of pip is available: 25.1.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
```

You'll now notice that the dependencies are in your lib folder for the venv

```
(.venv) macbookpro:pyproject mkwyche$ ls -l .venv/lib/python3.13/site-packages/
total 312
drwxr-xr-x   3 mkwyche  staff      96 Aug 13 02:33 __pycache__
drwxr-xr-x   6 mkwyche  staff     192 Aug 13 02:33 annotated_types
drwxr-xr-x   7 mkwyche  staff     224 Aug 13 02:33 annotated_types-0.7.0.dist-info
drwxr-xr-x  36 mkwyche  staff    1152 Aug 13 02:33 greenlet
drwxr-xr-x   8 mkwyche  staff     256 Aug 13 02:33 greenlet-3.2.4.dist-info
drwxr-xr-x   4 mkwyche  staff     128 Aug 13 02:33 hello_pyproject
drwxr-xr-x   8 mkwyche  staff     256 Aug 13 02:33 hello_pyproject-0.0.1.dist-info
drwxr-xr-x   9 mkwyche  staff     288 Aug 13 02:30 pip
drwxr-xr-x  10 mkwyche  staff     320 Aug 13 02:30 pip-25.1.1.dist-info
drwxr-xr-x  44 mkwyche  staff    1408 Aug 13 02:33 pydantic
drwxr-xr-x   8 mkwyche  staff     256 Aug 13 02:33 pydantic_core
drwxr-xr-x   7 mkwyche  staff     224 Aug 13 02:33 pydantic_core-2.33.2.dist-info
drwxr-xr-x   7 mkwyche  staff     224 Aug 13 02:33 pydantic-2.11.7.dist-info
drwxr-xr-x  23 mkwyche  staff     736 Aug 13 02:33 sqlalchemy
drwxr-xr-x   8 mkwyche  staff     256 Aug 13 02:33 sqlalchemy-2.0.43.dist-info
drwxr-xr-x   7 mkwyche  staff     224 Aug 13 02:33 typing_extensions-4.14.1.dist-info
-rw-r--r--   1 mkwyche  staff  157408 Aug 13 02:33 typing_extensions.py
drwxr-xr-x   8 mkwyche  staff     256 Aug 13 02:33 typing_inspection
drwxr-xr-x   7 mkwyche  staff     224 Aug 13 02:33 typing_inspection-0.4.1.dist-info
```

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
