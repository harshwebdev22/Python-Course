# 02 — Control Flow

`if`/`else`, loops, boolean logic — all conceptually the same as JS/PHP. Only
the syntax differs. Skipping the concepts, here's what's actually different.

## Indentation is syntax, not style

There are no `{}` blocks. Indentation (consistently 4 spaces, per PEP 8)
*is* how blocks are delimited. Get it wrong and the code means something
different, not just "ugly."

```python
if age >= 18:
    print("adult")
else:
    print("minor")
```

No parens required around the condition, and a colon `:` starts every block
(`if`, `for`, `while`, `def`, `class`, ...).

## Booleans / falsy values

`and`, `or`, `not` — spelled out, not `&&`/`||`/`!`.

Falsy values: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()` —
any "empty" container is falsy, same spirit as JS but it extends to all
built-in containers, not just a couple of primitives.

## `for` loops iterate over things, not counters

There is no C-style `for (i=0; i<n; i++)`. You loop over an iterable
directly:

```python
for fruit in ["apple", "banana"]:
    print(fruit)

for i in range(5):        # 0..4 — range() is Python's counting loop
    print(i)

for i, fruit in enumerate(["apple", "banana"]):  # index + value together
    print(i, fruit)
```

`range(start, stop, step)` is lazy (doesn't build a list) — closest JS
equivalent is manually writing the counting loop; PHP has nothing built-in
this idiomatic.

## No `switch`/`match` in older Python — `match` exists since 3.10

```python
match status:
    case 200:
        print("ok")
    case 404 | 500:       # multiple values, like `case 404: case 500:` fallthrough in JS but explicit
        print("error")
    case _:                # default
        print("unknown")
```
It also does structural pattern matching (destructuring), which `switch`
doesn't do in JS/PHP — worth knowing exists, but `if/elif` is still more
common in everyday Python code and totally fine to reach for instead.

## `while`/`break`/`continue` — same as you know, but loops have `else`

Python's oddest control-flow feature: `for`/`while` loops can have an `else`
clause that runs **only if the loop completed without hitting `break`**.
Rare in the wild, but you'll see it and should recognize it:

```python
for n in range(2, 10):
    if n % 7 == 0:
        break
else:
    print("no multiple of 7 found")  # runs because we didn't break
```

## Ternary is reordered

```python
label = "adult" if age >= 18 else "minor"   # value if condition else other_value
```

## Truthiness checks: prefer them over `== True`/`!= None`

```python
if items:            # not `if len(items) > 0:`
    ...
if value is None:     # `is`, not `==`, when checking against None/True/False singletons
    ...
```
