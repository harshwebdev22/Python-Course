"""Run me: python3 example.py"""

# No declarations — just assign.
name: str = "Harsh"
age: int = 30

# f-strings
print(f"{name} is {age}")
print(f"{age * 2 = }")  # debug shorthand -> prints "age * 2 = 60"

# No block scope: `x` leaks out of the `if`.
if True:
    x = 5
print(f"x after the if-block: {x}")

# Strong typing: this would raise TypeError if uncommented.
# print("3" + 3)
print(int("3") + 3)  # explicit conversion required

# tuple: immutable, fixed-size grouping
point: tuple[int, int] = (3, 4)
print(f"point = {point}")
# point[0] = 9  # would raise TypeError: 'tuple' object does not support item assignment

# dict: ordered, string (or any hashable) keys
user: dict[str, str | int] = {"name": "Harsh", "age": True}
print(user["name"])

# set: unique, unordered
tags: set[str] = {"python", "js", "python"}  # dup collapses
print(tags)

# None is the only "nothing" value
maybe_score: int | None = None
print(f"maybe_score is None: {maybe_score is None}")  # use `is`, not `==`, for None

# Multiple assignment / unpacking
a, b = 1, 2
a, b = b, a  # swap, no temp var
print(f"a={a}, b={b}")

first, *rest = [1, 2, 3, 4]
print(f"first={first}, rest={rest}")

# "Constant" — convention only, nothing stops reassignment
MAX_RETRIES: int = 3
print(f"MAX_RETRIES = {MAX_RETRIES}")
