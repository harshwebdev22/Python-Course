"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""

# 1. Write a class `Rectangle` with `__init__(self, width: float, height:
#    float)`, a `@property` called `area`, and a `__repr__` that prints
#    something like "Rectangle(3x4)". Create one and print both `.area`
#    and the object itself.


# 2. Write a base class `Vehicle` with `__init__(self, make: str)` and a
#    method `describe(self) -> str`. Write a subclass `Car(Vehicle)` that
#    adds a `doors: int` field via its own `__init__` (calling
#    `super().__init__()`), and overrides `describe` to include the door
#    count. Instantiate both and call `describe()` on each.


# 3. Rewrite the `Rectangle` class from #1 as a `@dataclass` instead,
#    keeping `width` and `height` as fields. Note what you get "for free"
#    now vs. what you had to write by hand before (you'll still need to
#    write `area` yourself — dataclasses don't generate methods, only
#    __init__/__repr__/__eq__ from fields).
