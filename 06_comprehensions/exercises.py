"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

# 1. Given `words = ["banana", "kiwi", "fig", "watermelon"]`, use a list
#    comprehension to build a list of only the words with more than 4
#    letters, uppercased.

words = ["banana", "kiwi", "fig", "watermelon"]
results = {word.upper() for word in words if len(word) > 4}
print(f"{results}")


# 2. Given `prices = {"apple": 1.5, "bread": 3.0, "milk": 2.2}`, use a dict
#    comprehension to build a new dict with the same keys but prices
#    increased by 10% (round to 2 decimal places).

prices = {"apple": 1.5, "bread": 3.0, "milk": 2.2}
new_prices = {item: round(price * 1.10, 2) for item, price in prices.items()}
print(f"{new_prices}")

# 3. Use a generator expression (no brackets) inside `any(...)` to check
#    whether any word in `words` (from #1) starts with the letter "f".
#    Then rewrite the same check as a set comprehension wrapped in `bool()`
#    just to see the difference in what gets built — and think about why
#    the generator version is the better choice here.

print(any({word.startswith('f') for word in words}))
print(bool({word.startswith('f') for word in words}))