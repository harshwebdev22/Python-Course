# Python from Scratch — for a JS/PHP dev

You already know how programming works. This course skips concepts you already
have (loops are loops, functions are functions, `if` is `if`) and focuses on
**Python's specific syntax and idioms** — the stuff that trips up people
coming from JS/PHP: significant whitespace, duck typing, comprehensions,
`self`, the import/packaging story, and Python's exception-based error model.

Each topic folder has three files:

- `topic.md` — concise explanation, assumes you already understand the
  underlying concept from JS/PHP.
- `example.py` — runnable code demonstrating it. Run with `python3 example.py`.
- `exercises.py` — 2–3 small practice prompts, no solutions. Write the code
  yourself, then run it.

Style note: all examples use modern Python conventions — PEP 8 formatting,
type hints with built-in generics (`list[str]`, `dict[str, int]`, `X | None`
instead of `Optional[X]`), f-strings, and `pathlib` instead of `os.path`.
That's how idiomatic Python is written today (3.10+), not how 2015-era
tutorials write it.

## Order and dependencies

Read top to bottom for the default path. Where two topics have no dependency
on each other, they're marked **(parallel)** — do them in either order, or
interleave.

| # | Topic | Depends on | Parallel with |
|---|-------|-----------|----------------|
| 01 | [Variables & Types](01_variables_and_types/topic.md) | — | — |
| 02 | [Control Flow](02_control_flow/topic.md) | 01 | — |
| 03 | [Functions](03_functions/topic.md) | 02 | — |
| 04 | [Modules & Imports](04_modules_and_imports/topic.md) | 03 | 06, 07 |
| 05 | [Virtual Envs & pip](05_venv_and_pip/topic.md) | 04 | 06, 07, 08 |
| 06 | [Comprehensions](06_comprehensions/topic.md) | 03 | 04, 05, 07 |
| 07 | [Classes vs JS/PHP OOP](07_classes_vs_oop/topic.md) | 03 | 04, 05, 06 |
| 08 | [Error Handling & Tracebacks](08_error_handling_tracebacks/topic.md) | 03 | 05, 06, 07 |
| 09 | [Debugging (`breakpoint()`/pdb)](09_debugging_pdb/topic.md) | 08 | — |
| 10 | [File I/O](10_file_io/topic.md) | 08 | 09 |
| 11 | [Async/Await](11_async_await/topic.md) | 03, 08 | — |

**The hard prerequisite chain is: 01 → 02 → 03 → 08 → 11.**
Everything else (04/05 the packaging track, 06 comprehensions, 07 classes,
09/10 which both just need error handling from 08) branches off that spine
and can be done in whatever order you like once its one dependency is met.

Practical suggestion: do 01–03 in order, then knock out 04+05 together
(they're one "packaging" story), then 06 and 07 in either order, then
08 → 09 → 10 as a debugging/IO cluster, and finish with 11.

## Setup

You need Python 3.11+ (for the type-hint syntax used here). Check with:

```bash
python3 --version
```

Nothing else is required until [05_venv_and_pip](05_venv_and_pip/topic.md) —
every example before that uses only the standard library.
