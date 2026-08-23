# 09 — Debugging with `breakpoint()` / pdb

You know breakpoints from browser devtools / an IDE debugger. Python has a
built-in, no-setup, terminal-based equivalent baked into the language
itself — you don't need an IDE or extension for the basics.

## `breakpoint()` — drop into a debugger from anywhere

```python
def calculate(a: int, b: int) -> int:
    total = a + b
    breakpoint()   # execution pauses HERE, drops you into an interactive prompt
    return total * 2
```

Run the script normally (`python3 file.py`). When execution reaches
`breakpoint()`, it stops and gives you a `(Pdb)` prompt right there in your
terminal — no separate debug configuration, no "attach debugger" step. This
is the standard, modern (3.7+) way to set a breakpoint; older code you'll
see online uses `import pdb; pdb.set_trace()` instead — same effect,
`breakpoint()` is just the shorter modern spelling.

## The `(Pdb)` prompt — commands to know

At the prompt, type these (single letters, mostly):

| Command | Does |
|---|---|
| `n` (next) | run the next line, step **over** function calls |
| `s` (step) | step **into** a function call |
| `c` (continue) | resume running until the next `breakpoint()` or program end |
| `l` (list) | show source code around the current line |
| `p expr` | print the value of an expression, e.g. `p total` |
| `pp expr` | pretty-print (good for dicts/lists) |
| `w` (where) | show the current call stack |
| `q` (quit) | abort execution entirely |
| just typing a variable name | also prints it, no `p` needed |
| any Python expression | evaluated live in the current scope — you can even reassign variables |

The prompt is a **live Python REPL scoped to exactly where you paused** —
you can inspect *and mutate* state, call functions, whatever you'd do in a
normal Python shell.

## Conditional breakpoints — just wrap it in an `if`

No special "conditional breakpoint" UI needed; it's just code:

```python
for i in range(100):
    if i == 42:
        breakpoint()   # only pauses on this one iteration
```

## Post-mortem debugging: inspect a crash after the fact

```bash
python3 -m pdb -c continue example.py
```
Runs the script, and if it crashes with an unhandled exception, drops you
into pdb *at the point of the crash* instead of just printing a traceback
and exiting — useful when you don't want to add a `breakpoint()` line
in advance.

## Removing breakpoints before committing

Search for `breakpoint()` before you commit — same discipline as removing
stray `console.log`/`var_dump` calls. Nothing stops you from shipping one
accidentally; there's no lint-by-default warning unless your tooling adds
one.
