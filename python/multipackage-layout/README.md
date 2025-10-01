# Multimodule Project Layout

## Commands

In the below example you can see I'm able to pull in the Appetizers Enum from the appetizer's project not using src at all.

```
macbookpro:customer mkwyche$ uv run src/customer/main.py
Hello from customer!
Appetizer.WINGS
Appetizer.CALAMARI
```

## Notes

* Creating project via `uv` can be done with `uv init`. Docs for this are [here](https://docs.astral.sh/uv/concepts/projects/init/#applications)

```
# This will give you the package
uv init --package example-pkg
```

You'll need to add this to get the package working correctly so you don't need src at the toplevel:

```
[tool.uv]
packages = [{include = "appetizer", from = "src"}]
```

* To add this as a dependency to another module run:

```
uv add ../appetizer/
```

Which will add the dependency to your toml

```toml
dependencies = [
    "appetizer",
]

[tool.uv.sources]
appetizer = { path = "../appetizer" }
```