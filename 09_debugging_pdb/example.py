"""
Run me: python3 example.py

When execution hits breakpoint(), you'll get a (Pdb) prompt in your
terminal. Try these, in order:
    p a          -> prints the value of `a`
    p b
    n            -> steps to the next line
    p total
    c            -> continues execution to the end
"""


def calculate(a: int, b: int) -> int:
    total = a + b
    breakpoint()  # execution pauses HERE
    return total * 2


print("before calculate()")
result = calculate(3, 4)
print(f"result: {result}")

# Conditional breakpoint: only pauses on one specific iteration
for i in range(5):
    if i == 3:
        breakpoint()  # try `p i`, then `c` to finish the loop
    print(f"i = {i}")

print("done")
