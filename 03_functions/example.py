"""Run me: python3 example.py"""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


print(add(2, 3))
print(add.__doc__)  # docstrings are introspectable, not just comments


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


print(greet("Harsh"))
print(greet("Harsh", greeting="Hi"))
print(greet(name="Harsh", greeting="Hi"))


def total(*numbers: int) -> int:
    return sum(numbers)


print(total(1, 2, 3, 4))


def build(**fields: str) -> dict[str, str]:
    return fields


print(build(name="Harsh", role="dev"))

# Unpacking at the call site
nums = (10, 20)
print(add(*nums))

kwargs = {"a": 1, "b": 2}
print(add(**kwargs))


def connect(host: str, *, port: int = 5432) -> str:
    return f"{host}:{port}"


print(connect("localhost", port=5433))  # port must be passed by name


# Lambda — single expression only
square = lambda x: x * x
print(square(5))

words = ["banana", "fig", "apple"]
print(sorted(words, key=lambda w: len(w)))


# Closures: reading is free, rebinding needs `nonlocal`
def make_counter():
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter(), counter(), counter())
