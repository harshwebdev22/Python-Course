"""Run me: python3 example.py"""

nums = [1, 2, 3, 4, 5]

# Basic list comprehension
squares = [n * n for n in nums]
print(f"squares: {squares}")

# With a filter condition
evens_squared = [n * n for n in nums if n % 2 == 0]
print(f"evens_squared: {evens_squared}")

# The manual for-loop equivalent, for comparison
result = []
for n in nums:
    if n % 2 == 0:
        result.append(n * n)
print(f"manual loop gives the same thing: {result == evens_squared}")

# Nested loops in a comprehension
pairs = [(x, y) for x in range(3) for y in range(2)]
print(f"pairs: {pairs}")

# Dict comprehension
names = ["alice", "bob", "cassandra"]
lengths = {name: len(name) for name in names}
print(f"lengths: {lengths}")

# Set comprehension
unique_lengths = {len(name) for name in names}
print(f"unique_lengths: {unique_lengths}")

# Generator expression — lazy, no intermediate list
total = sum(n * n for n in nums)
print(f"total: {total}")

# When it gets too dense, prefer a plain loop instead — this is a smell:
# messy = [f(x) if cond(x) else g(x) for x in data if other_cond(x) for y in x.items]
