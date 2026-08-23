# 11 — Async/Await Basics

`async`/`await` exist in Python with nearly identical *keywords* to JS. The
underlying execution model is different enough to be worth understanding
before you write real async Python code.

## The keywords look the same

```python
async def fetch_data() -> str:      # `async def`, not `async function`
    await some_coroutine()           # `await` works the same way syntactically
    return "done"
```

## The big difference: nothing runs concurrently by accident

In JS, `async`/`await` sits on top of an event loop that's *always running*
— every Promise you create is scheduled automatically, top-level `await`
works in modules, and the runtime just handles it.

In Python, `asyncio` (the standard async library) is **opt-in and explicit**.
Calling an `async def` function does **not** run it — it returns a
*coroutine object*, inert until something actually drives it:

```python
async def greet() -> str:
    return "hello"

result = greet()          # this is a coroutine object, NOT "hello" — nothing has run yet!
print(result)              # <coroutine object greet at 0x...>
```

You need an event loop to actually run it. At the top level of a script,
that's `asyncio.run()`:

```python
import asyncio

async def greet() -> str:
    return "hello"

result = asyncio.run(greet())   # THIS actually runs it
print(result)                    # "hello"
```
`asyncio.run()` is roughly Python's equivalent of Node auto-running your
top-level module's event loop — except in Python you call it explicitly,
once, as your program's entry point.

## Running things concurrently: `asyncio.gather` / `TaskGroup`

`await`-ing coroutines one after another, plainly, still runs them
**sequentially** — same as awaiting Promises one at a time in JS. To
actually run multiple things concurrently, you need to say so explicitly:

```python
import asyncio

async def task(name: str, delay: float) -> str:
    await asyncio.sleep(delay)   # non-blocking sleep — like a Promise-based setTimeout
    return f"{name} done"

async def main() -> None:
    # sequential — takes ~3 seconds total
    a = await task("A", 1)
    b = await task("B", 2)

    # concurrent — takes ~2 seconds total (the max, not the sum)
    results = await asyncio.gather(task("A", 1), task("B", 2))
    print(results)

asyncio.run(main())
```
Closest JS equivalent to `asyncio.gather` is `Promise.all`.

## Why this matters: `async` doesn't mean "parallel," and it doesn't mean "fast" for CPU work

Same caveat as JS: `async`/`await` gives you concurrency for **I/O-bound**
work (network calls, file/database waits) via cooperative multitasking on a
single thread — it does *not* give you parallel CPU execution. CPU-heavy
work in Python needs a different tool entirely (`multiprocessing` /
`concurrent.futures`), out of scope here — just know `asyncio` won't speed
up a tight numeric loop.

## You can't `await` outside an `async def`

Unlike JS (which allows top-level `await` in ES modules), Python requires
every `await` to be inside an `async def` function. There's no script-level
top-level await — `asyncio.run(main())` is the standard entry point
pattern you'll use in essentially every async script.
