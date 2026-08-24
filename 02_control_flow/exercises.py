"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

# 1. Given `scores = [55, 82, 91, 40, 76]`, loop over it with `enumerate`
#    and print "index N: PASS" if the score is >= 60, else "index N: FAIL".

for n, score in enumerate([55, 82, 91, 40, 76]):
    if score >= 60:
        print(f"index {n}: PASS")
    else:
        print(f"index {n}: FAIL")

# 2. Write a `while` loop that prints numbers from 10 down to 1, but stops
#    early (via `break`) if it hits a number divisible by 4. Add a `while
#    ... else` clause that prints "never hit a multiple of 4" — trigger it
#    by changing the starting number so the break never fires.

n = 3
# n = 10
while n >= 1:
    if n % 4 == 0:
        break

    print(f"number {n}")
    n -= 1

else:
    print(f"never hit a multiple of 4")


# 3. Using `match`/`case`, write a function-free block that takes a variable
#    `day = "sat"` and prints "weekend" for "sat"/"sun", "weekday" for
#    anything else, using a single case that matches multiple values for
#    the weekend case.

day = "sat"
match day:
    case "sat" | "sun":
        print(f"weekend")
    case _:
        print(f"weekday")