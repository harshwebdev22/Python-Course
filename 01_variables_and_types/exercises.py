"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

# 1. Create three variables with type hints: a `str` name, an `int` year of
#    birth, and a `float` height in meters. Print a single f-string sentence
#    using all three (e.g. "Harsh was born in 1994 and is 1.78m tall").

name: str = "Harsh"
dob: int = 2004
height: float = 1.69
print(f"{name} was born in {dob} and is {height}m tall.")

# 2. Given `pair = (10, 20)`, unpack it into two variables `low` and `high`
#    in one line, then swap them using Python's swap idiom (no temp
#    variable). Print both before and after.

low , high = (10, 20)
low , high = high, low
print(f"low={low} & high={high}")

# 3. Create a dict called `inventory` mapping three item names (str) to
#    quantities (int). Then create a `set` from `inventory.keys()` and print
#    it. (Look up how to build a set from an iterable if you don't already
#    know — this is a good first "read the docs" exercise.)

inventory: dict[set[str], set[int]] = {"Banana": 1, "Apple": 3, "Almonds": 50}
item_names: set[str] = set(inventory.keys())
item_quantities: set[int] = set(inventory.values())
print(f"{inventory}")
print(f"{item_names}")
print(f"{item_quantities}")