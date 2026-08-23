# 04 — Modules & Imports

Every `.py` file is automatically a module — no `export` keyword needed
(unlike JS's ESM, unlike PHP's `require`). Anything defined at module level
(functions, classes, variables) is importable by name.

## Importing

```python
import math                       # whole module, access via math.sqrt(...)
from math import sqrt, pi         # named imports, like JS's `import { sqrt } from`
from math import sqrt as square_root  # alias
import numpy as np                # module alias — extremely common convention
```

There's no default export / named export distinction like ESM. Everything at
module top level is just "there," and you pick what to pull in.

## Your own modules: filename = module name

```
project/
  main.py
  helpers.py
```

```python
# main.py
import helpers
from helpers import format_name

helpers.format_name("harsh")
```

No `require`/`export` boilerplate in `helpers.py` — every top-level name is
automatically importable.

## Packages: a folder becomes a package via `__init__.py`

```
project/
  mypackage/
    __init__.py      # marks this folder as a package (can be empty)
    utils.py
  main.py
```

```python
from mypackage import utils
from mypackage.utils import some_function
```

Modern Python (3.3+) technically allows "namespace packages" without
`__init__.py`, but including an (even empty) `__init__.py` is still the
common, unambiguous convention — do it.

## `if __name__ == "__main__":` — Python's script-vs-import guard

Every module has a `__name__`. When you run a file directly
(`python3 file.py`), Python sets `__name__ = "__main__"` in it. When the
same file is *imported* by another module, `__name__` is the module's
filename instead. So:

```python
def main() -> None:
    print("running as a script")

if __name__ == "__main__":
    main()
```

This is the closest thing Python has to PHP's separation of "included file"
vs. "entry point," or Node's `require.main === module`. Put this guard at
the bottom of any file that should be both importable *and* runnable
directly — library code with no guard just runs its top-level code on
import, which is rarely what you want for anything beyond definitions.

## Absolute vs relative imports inside a package

```python
# inside mypackage/utils.py, importing a sibling module:
from . import other_module        # relative import — current package
from .other_module import helper  # relative import of a name
from mypackage import other_module  # absolute import — also works
```

Prefer absolute imports for anything outside the immediate package; relative
imports (`.`, `..`) are fine within a package but get confusing fast if
overused.

## The standard library is large — check it before reaching for a package

`math`, `random`, `datetime`, `json`, `pathlib`, `collections`, `itertools`,
`re`, `os`, `sys` cover a lot of what you'd otherwise `npm install` for.
Third-party packages (the `pip`/PyPI equivalent of `npm`) are covered next in
[05_venv_and_pip](../05_venv_and_pip/topic.md).
