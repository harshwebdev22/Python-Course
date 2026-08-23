# 08 — Error Handling & Reading Tracebacks

`try`/`catch` exists conceptually in both JS and PHP — Python's version has
different keywords and a genuinely useful extra clause (`else`), plus its
own error hierarchy and stack-trace format worth learning to read fast.

## `try` / `except` / `else` / `finally`

```python
try:
    result = 10 / divisor
except ZeroDivisionError:              # `except`, not `catch`
    print("can't divide by zero")
except (TypeError, ValueError) as e:   # multiple types in a tuple; `as e` binds the exception
    print(f"bad input: {e}")
else:
    print(f"result: {result}")         # runs only if NO exception was raised — no JS/PHP equivalent
finally:
    print("always runs")               # same as JS/PHP finally
```

`else` has no direct JS/PHP counterpart — it's Python's way of separating
"the code that might fail" from "the code that should only run on success,"
without nesting it inside the `try` block (where it might swallow *its own*
unrelated errors into the same `except`).

## Catch specific exceptions — avoid bare `except:`

```python
try:
    ...
except Exception as e:   # catches (almost) everything — usually too broad
    ...
```
Bare `except:` (no type at all) catches literally everything, including
`KeyboardInterrupt` — avoid it. Prefer naming the specific exception type(s)
you actually expect, same discipline as catching specific error classes in
JS/PHP rather than a blanket `catch (Exception $e)`.

## Raising exceptions

```python
def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise ValueError(f"insufficient funds: {amount} > {balance}")  # `raise`, not `throw`
    return balance - amount
```

## Custom exceptions: subclass `Exception`

```python
class InsufficientFundsError(Exception):
    pass

raise InsufficientFundsError("not enough money")
```
Equivalent to `class MyError extends Error` (JS) / `extends Exception`
(PHP) — same idea, Python just calls the base class `Exception`.

## Common built-in exception types (roughly analogous to JS/PHP's)

| Python | Roughly like |
|---|---|
| `ValueError` | wrong value, right type |
| `TypeError` | wrong type entirely |
| `KeyError` | missing dict key |
| `IndexError` | out-of-range list index |
| `FileNotFoundError` | missing file |
| `AttributeError` | accessing a missing attribute/method |
| `ZeroDivisionError` | dividing by zero |

## Reading a traceback

This is the part that actually differs day-to-day: Python tracebacks read
**top to bottom, outermost call first, actual error last** — the opposite
end from where you'd look in most JS stack traces at a glance:

```
Traceback (most recent call last):
  File "example.py", line 12, in <module>
    result = divide(10, 0)
  File "example.py", line 5, in divide
    return a / b
ZeroDivisionError: division by zero
```

Read it bottom-up: the **last line** is the actual exception type and
message — start there. Then walk upward through the `File "...", line N, in
funcname` entries to see the call chain that led there (bottom entry = where
it broke, top entry = where the chain started). The line quoted under each
`File` entry is the actual source line — often enough to spot the bug
without opening the file.

## Exception chaining: `raise ... from ...`

```python
try:
    int("not a number")
except ValueError as e:
    raise RuntimeError("config parsing failed") from e   # keeps the original traceback attached
```
Shows up in tracebacks as "The above exception was the direct cause of the
following exception" — preserves the root cause instead of hiding it,
unlike a re-thrown generic error that loses the original stack.
