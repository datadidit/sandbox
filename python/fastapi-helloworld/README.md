# Simple FastAPI pclear

## Commands

### Setup

```
# Create virtualenv
python -m venv .venv
# Install uv
pip install uv
```

### Run the Application 

```
(.venv) macbookpro:fastapi-helloworld mkwyche$ uv run fastapi dev src/hello_api/asgi.py

   FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from /Users/mkwyche/workspace/sandbox/python/uv/fastapi-helloworld/src

    module   📁 hello_api
             ├── 🐍 __init__.py
             └── 🐍 asgi.py

      code   Importing the FastAPI app object from the module with the following code:

             from hello_api.asgi import app

       app   Using import string: hello_api.asgi:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories: ['/Users/mkwyche/workspace/sandbox/python/uv/fastapi-helloworld']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [9238] using WatchFiles
      INFO   Started server process [9241]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```

### Test the Application

```
(.venv) macbookpro:fastapi-helloworld mkwyche$ uv run pytest
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/mkwyche/workspace/sandbox/python/uv/fastapi-helloworld
configfile: pyproject.toml
plugins: anyio-4.10.0
collected 1 item

tests/test_app.py .                                                                                                                                                                                                  [100%]

==================================================================================================== 1 passed in 0.41s =====================================================================================================
```