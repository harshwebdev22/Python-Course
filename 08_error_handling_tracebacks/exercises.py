"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

# 1. Write a function `parse_age(text: str) -> int` that converts a string
#    to an int and raises a `ValueError` with a clear message if it's
#    negative. Call it in a try/except that prints either the parsed age or
#    the error message. Test it with "25", "-5", and "abc" (the last one
#    will raise a *different* exception type than your ValueError — catch
#    that one too and notice which built-in type it is).
class NegativeAgeError(Exception):
    pass

def parse_age(text: str) -> int:
    try:
        age = int(text)
    except ValueError as e:
        raise NegativeAgeError(f"Invalid age: {e}") from e
        
    if age < 0:
        raise NegativeAgeError(f"Age cannot be negative")
    return age

# try:
#     print(parse_age("25"))
#     print(parse_age("-5"))
#     print(parse_age("abc"))
# except ValueError as e:
#     print(f'Parsing error: {e}')


# 2. Deliberately write code that raises an unhandled exception (e.g. index
#    into an empty list). Run the file, and practice reading the traceback:
#    write a one-line comment identifying (a) the exception type, (b) the
#    line number where it broke.

# numbers = []
# print(numbers[0])

# 3. Create a custom exception `NegativeAgeError(Exception)`. Rewrite
#    `parse_age` from #1 to raise it instead of a plain ValueError,
#    chaining it with `from` if the original failure came from `int()`
#    raising a ValueError. Catch and print `.__cause__` if present.



try:
    print(parse_age("25"))
    # print(parse_age("-5"))
    print(parse_age("abc"))
except NegativeAgeError as e:
    print(f'Parsing error: {e}')
    print(f'Cause: {e.__cause__}')
    