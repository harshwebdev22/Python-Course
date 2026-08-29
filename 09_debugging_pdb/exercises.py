"""
Practice — write the code yourself under each prompt, then run this file
and actually use the (Pdb) prompt for each one. No solutions provided.
"""

# 1. Write a function `buggy_average(numbers: list[float]) -> float` that
#    (intentionally, for practice) divides by the wrong length somewhere,
#    e.g. `len(numbers) - 1`. Drop a `breakpoint()` right before the
#    division, call the function with [10, 20, 30], and at the (Pdb)
#    prompt use `p` to inspect the values involved before continuing with
#    `c`. Fix the bug once you've found it with the debugger.

def buggy_average(numbers: list[float]) -> float:
    total = sum(numbers)
    length = len(numbers) - 1
    breakpoint()
    return total / length

print(buggy_average([10, 20, 30]))


# 2. Write a loop over `range(10)` with a `breakpoint()` that only triggers
#    when the loop variable is divisible by 3 (an `if` check, like the
#    example). Use `n` (next) a few times at the prompt to step through
#    several lines before typing `c` to let it continue to the next
#    trigger.

for i in range(10):
    if i % 3 == 0:
        breakpoint()
    print(f"i {i}")

# 3. Run this file with `python3 -m pdb -c continue exercises.py` instead
#    of a plain `python3 exercises.py`, after temporarily adding a line
#    that raises an exception (e.g. `1 / 0`) somewhere below with no
#    breakpoint() at all. Confirm you land in a live pdb prompt at the
#    crash site, use `p` to inspect any nearby variables, then `q` to quit.

print(1 / 0)