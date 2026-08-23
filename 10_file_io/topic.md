# 10 — Basic File I/O

Reading/writing files is a familiar concept. Python's take: the `with`
statement for automatic cleanup, and `pathlib` as the modern way to handle
paths instead of string concatenation.

## `open()` + `with` — automatic closing

```python
with open("data.txt", "r") as f:   # "with" = context manager, closes the file automatically
    contents = f.read()
# file is already closed here, even if an exception was raised inside the block
```

`with` is Python's answer to "don't forget to close the file" / "don't
forget to release the resource" — conceptually like a `try/finally` that
calls `.close()` for you, but built into the language as a reusable pattern
(any object implementing the *context manager* protocol works with `with`,
not just files).

Never do `f = open(...)` without `with` (or a manual `try/finally`) in real
code — an exception between open and close would leak the file handle.

## Modes

| Mode | Meaning |
|---|---|
| `"r"` | read (default) |
| `"w"` | write, truncates existing content |
| `"a"` | append |
| `"r+"` | read + write, no truncate |
| add `"b"` (e.g. `"rb"`) | binary mode |

## Reading

```python
with open("data.txt") as f:
    contents = f.read()          # whole file as one string

with open("data.txt") as f:
    lines = f.readlines()        # list of lines (each ending in \n)

with open("data.txt") as f:
    for line in f:                # iterate line-by-line — memory-efficient for big files
        print(line.strip())       # .strip() removes the trailing newline
```

## Writing

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.writelines(["second\n", "third\n"])
```

## `pathlib` — the modern way to handle paths (prefer over `os.path`)

```python
from pathlib import Path

p = Path("data") / "input.txt"    # `/` is overloaded to join paths — no string concatenation
print(p.exists())
print(p.name, p.suffix, p.parent)

text = p.read_text()               # shortcut: read a whole file without `open`/`with`
p.write_text("new content")        # shortcut: write a whole file in one call
```
`pathlib.Path` objects work cross-platform automatically (handles `/` vs
`\` for you) — closest analog is Node's `path` module, but object-oriented
and with these one-shot `read_text()`/`write_text()` convenience methods
that neither JS nor PHP have built in.

## JSON — very common, one import away

```python
import json

data = {"name": "Harsh", "age": 30}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)   # like JSON.stringify + fs.writeFile combined

with open("data.json") as f:
    loaded = json.load(f)           # like JSON.parse + fs.readFile combined

json_string = json.dumps(data)      # to a string, not a file
parsed = json.loads(json_string)    # from a string
```
`dump`/`load` work with a file object; `dumps`/`loads` (with the trailing
`s`) work with strings — an easy pair to mix up at first.
