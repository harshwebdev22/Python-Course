"""Run me: python3 example.py"""

age = 20

# Indentation-delimited if/else, colon starts the block
if age >= 18:
    print("adult")
else:
    print("minor")

# Ternary — reordered vs JS's `cond ? a : b`
label = "adult" if age >= 18 else "minor"
print(f"label = {label}")

# for-in over an iterable, not a counter
for fruit in ["apple", "banana"]:
    print(f"fruit: {fruit}")

# range() for counting loops
for i in range(5):  # 0..4
    print(f"i = {i}")

# enumerate() gives index + value together
for i, fruit in enumerate(["apple", "banana"]):
    print(f"{i}: {fruit}")

# match/case (structural pattern matching, 3.10+)
status = 404
match status:
    case 200:
        print("ok")
    case 404 | 500:
        print("error")
    case _:
        print("unknown")

# while/else: else runs only if the loop finishes without `break`
for n in range(2, 10):
    if n % 7 == 0:
        print(f"found a multiple of 7: {n}")
        break
else:
    print("no multiple of 7 found")

# Truthiness on containers
items: list[int] = []
if not items:
    print("items is empty")

value = None
if value is None:  # `is`, not `==`, for None
    print("value is None")
