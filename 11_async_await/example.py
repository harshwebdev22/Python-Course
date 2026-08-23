"""Run me: python3 example.py"""

import asyncio
import time


async def greet() -> str:
    return "hello"


# Calling an async function just gives you a coroutine object — nothing has run.
uncalled = greet()
print(f"before running: {uncalled}")
uncalled.close()  # avoid a "coroutine was never awaited" warning since we won't run this one


async def task(name: str, delay: float) -> str:
    await asyncio.sleep(delay)  # non-blocking sleep
    return f"{name} done after {delay}s"


async def sequential_demo() -> None:
    start = time.perf_counter()
    a = await task("A", 1)
    b = await task("B", 1)
    elapsed = time.perf_counter() - start
    print(f"sequential: {a}, {b} — took ~{elapsed:.1f}s (should be ~2s)")


async def concurrent_demo() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(task("A", 1), task("B", 1))
    elapsed = time.perf_counter() - start
    print(f"concurrent: {results} — took ~{elapsed:.1f}s (should be ~1s, not 2s)")


async def main() -> None:
    result = await greet()
    print(f"awaited: {result}")

    await sequential_demo()
    await concurrent_demo()


asyncio.run(main())  # the actual entry point — nothing above runs without this
