"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

# 1. Write a function `describe_pet(name: str, species: str = "dog") -> str`
#    that returns a sentence like "Rex is a dog". Call it three ways: with
#    only the required arg, with both positional, and with `species` passed
#    by keyword.

def describe_pet(name: str, species: str = "dog") -> str:
    return f"{name} is a {species}"

print(describe_pet("German Shefherd"))
print(describe_pet("German Shefherd", "dog"))
print(describe_pet("German Shefherd", species="dog"))


# 2. Write a function `average(*numbers: float) -> float` that returns the
#    mean of any number of arguments passed in (handle the zero-arguments
#    case however you think is reasonable). Call it with 0, 1, and 4
#    numbers.

def average(*numbers: float) -> float:
    if len(numbers) is 0:
        return 0.0
    return sum(numbers) / len(numbers)

print(average())
print(average(5))
print(average(1, 2, 3, 4))

# 3. Write a function `make_multiplier(factor: int)` that returns a closure
#    which multiplies its argument by `factor`. Create `double =
#    make_multiplier(2)` and `triple = make_multiplier(3)`, and print
#    `double(5)` and `triple(5)`. (No `nonlocal` needed here — think about
#    why, versus the counter example.)

def make_multiplier(factor: int) -> int:
    def multiplier(n: int) -> int:
        return n * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))