# 03 — Functions

Functions-as-values, closures, higher-order functions — same concepts as
JS. Different syntax, and a few Python-specific parameter features PHP/JS
don't have.

## Definition

```python
def add(a: int, b: int) -> int:   # -> return type hint
    return a + b
```

`def`, not `function`. Return type hint goes after `->`. No braces — body is
the indented block.

## Default & keyword arguments (bigger deal than in JS/PHP)

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

greet("Harsh")                       # positional
greet("Harsh", greeting="Hi")        # keyword — self-documenting at call site
greet(name="Harsh", greeting="Hi")   # any/all args can be passed by name
```

Any parameter can be passed by name at the call site, in any order, unless
the function explicitly forbids it. This is used constantly in idiomatic
Python (`sorted(items, key=lambda x: x.age, reverse=True)`) — get comfortable
reading `name=value` in call sites, it's not object-literal shorthand, it's
just naming an argument.

## `*args` and `**kwargs` — variadic parameters

```python
def total(*numbers: int) -> int:          # collects extra positional args into a tuple
    return sum(numbers)

def build(**fields: str) -> dict[str, str]:  # collects extra keyword args into a dict
    return fields

total(1, 2, 3)                # 6
build(name="Harsh", role="dev")  # {"name": "Harsh", "role": "dev"}
```

Closest JS equivalent is `...args` rest params for `*args`; `**kwargs` has
no direct JS/PHP analog (closest: destructuring an options object) — but
it's everywhere in Python, so recognize the syntax on sight.

## `**` and `*` for unpacking at the *call* site too

```python
def add(a: int, b: int) -> int:
    return a + b

nums = (1, 2)
add(*nums)          # unpacks tuple/list into positional args

kwargs = {"a": 1, "b": 2}
add(**kwargs)        # unpacks dict into keyword args
```

## Keyword-only and positional-only parameters

```python
def connect(host: str, *, port: int = 5432) -> None:  # bare * forces everything after it to be keyword-only
    ...

connect("localhost", port=5433)   # required
# connect("localhost", 5433)       # TypeError — port must be named
```
No JS/PHP equivalent worth comparing to — this is a Python-only guardrail
for API clarity. You'll see it in library signatures often.

## Lambdas: single expression only

```python
square = lambda x: x * x   # like a JS arrow fn, but no block body, no statements
sorted(words, key=lambda w: len(w))
```
Anything beyond one expression, just use a regular `def` — lambdas are
intentionally limited in Python (no multi-line, no `if`/`for` statements
inside).

## Docstrings, not JSDoc

```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b
```
A string literal as the first statement in the body **is** the
documentation (accessible via `add.__doc__`, shown by `help(add)`) — not a
comment convention layered on top like JSDoc.

## Closures work the same, but rebinding an outer variable needs `nonlocal`

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count   # without this, `count += 1` would raise UnboundLocalError
        count += 1
        return count
    return increment
```
Reading an outer variable from a closure works with no keyword. *Reassigning*
it requires `nonlocal` (or `global` at module level) — Python needs to know
upfront whether a name inside a function is local or refers to an enclosing
scope.
