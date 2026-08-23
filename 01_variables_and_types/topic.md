# 01 — Variables & Types

## No `var`/`let`/`const`, no declarations

Just assign. The name springs into existence in whatever scope you assigned
it in.

```python
name = "Harsh"   # no let/const/var, no semicolon
```

Scope is per-function (and module/class), **not** per-block. Unlike JS, an
`if`/`for` block does **not** create a new scope:

```python
if True:
    x = 5
print(x)  # 5 — still visible, no block scoping like `let` gives you in JS
```

## Everything is an object, and types are dynamic but strong

Like JS, no declared type. Unlike JS, Python won't silently coerce types for
you: `"3" + 3` raises `TypeError` (compare JS's `"3" + 3 === "33"`, or PHP's
looser coercion). You must convert explicitly: `int("3") + 3`.

## Core built-in types you'll actually use

| Python | Closest JS/PHP equivalent | Note |
|---|---|---|
| `int` | `number` (integer) | Arbitrary precision — never overflows |
| `float` | `number` (float) | |
| `str` | `string` | Immutable, single/double quotes are identical |
| `bool` | `boolean` | `True`/`False` — capitalized |
| `None` | `null`/`undefined` | One value, not two |
| `list` | `Array` | Mutable, ordered |
| `tuple` | — (closest: `Object.freeze([...])`) | Immutable, ordered |
| `dict` | plain object / assoc array | Ordered (insertion order, guaranteed since 3.7) |
| `set` | `Set` | Unordered, unique |

Nothing here is worth dwelling on except:

- **`tuple`**: a first-class immutable sequence, `(1, 2, 3)`. Used constantly
  for fixed-size groupings and multiple return values — there's no
  destructuring-a-frozen-array ceremony like in JS.
- **One `None`**, not `null` + `undefined`. An unset variable doesn't exist
  at all (referencing it raises `NameError`), it's never silently `None`.

## f-strings, not template literals

```python
age = 30
print(f"{name} is {age}")       # f-string — like JS `${}` but with an f prefix
print(f"{age * 2 = }")          # debug shorthand: prints "age * 2 = 60"
```

## Type hints (optional, but standard in modern Python)

Python stays dynamically typed at runtime — hints are not enforced unless you
run a checker (mypy, pyright) or a validation library. But idiomatic modern
code hints everything, because tooling (autocomplete, linters, refactors)
depends on it.

```python
name: str = "Harsh"
age: int = 30
maybe_score: int | None = None      # instead of Optional[int] — modern (3.10+) syntax
scores: list[int] = [1, 2, 3]       # built-in generics, not typing.List
user: dict[str, str] = {"name": "Harsh"}
```

Function signatures are where hints earn their keep — see
[03_functions](../03_functions/topic.md).

## Multiple assignment & unpacking

```python
a, b = 1, 2
a, b = b, a          # swap, no temp variable
first, *rest = [1, 2, 3, 4]   # *rest is like JS's ...rest, but in destructuring position
```

## Constants: convention, not enforcement

Python has no `const`. By convention, module-level "constants" are
`UPPER_SNAKE_CASE` and everyone agrees not to reassign them — nothing stops
you at runtime.

```python
MAX_RETRIES = 3
```
