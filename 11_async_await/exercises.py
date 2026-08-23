"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

import asyncio

# 1. Write an async function `fetch_user(user_id: int) -> dict` that
#    `await`s `asyncio.sleep(1)` and then returns a fake dict like
#    {"id": user_id, "name": f"user-{user_id}"}. Write an async `main()`
#    that awaits it for a single id and prints the result, run via
#    `asyncio.run(main())`.


# 2. Extend `main()` to fetch 3 different user ids sequentially (three
#    separate `await fetch_user(...)` calls) and time it with
#    `time.perf_counter()` before/after. Then rewrite the same 3 fetches
#    using `asyncio.gather(...)` and compare the elapsed time printed for
#    each approach.


# 3. Try calling `fetch_user(1)` directly at module level (outside any
#    async function, outside asyncio.run) and print what you get back.
#    Confirm it's a coroutine object, not a dict — then explain in a
#    one-line comment why, based on what you just read.
