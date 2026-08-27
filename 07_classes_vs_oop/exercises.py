"""
Practice — write the code yourself under each prompt, then run this file.
No solutions provided.
"""
from dataclasses import dataclass

# 1. Write a class `Rectangle` with `__init__(self, width: float, height:
#    float)`, a `@property` called `area`, and a `__repr__` that prints
#    something like "Rectangle(3x4)". Create one and print both `.area`
#    and the object itself.
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width  
        self.height = height
    
    @property
    def area(self) -> float:
        return self.width * self.height
    
    def __repr__(self) -> str:
        return f"Rectangle({self.width}x{self.height})"  

    
rectangle = Rectangle(3, 4)
print(rectangle)
print(rectangle.area)

# 2. Write a base class `Vehicle` with `__init__(self, make: str)` and a
#    method `describe(self) -> str`. Write a subclass `Car(Vehicle)` that
#    adds a `doors: int` field via its own `__init__` (calling
#    `super().__init__()`), and overrides `describe` to include the door
#    count. Instantiate both and call `describe()` on each.

class Vehicle:
    def __init__(self, make: str):
        self.make = make
        
    def describe(self) -> str:
        return f"Vehicle is {self.make}"
        
class Car(Vehicle):
    def __init__(self, make: str, doors: int) -> None:
        super().__init__(make)
        self.doors = doors
        
    def describe(self) -> str:
        return f"{self.make} has {self.doors} doors."
        
vehicle = Vehicle("Mercedes")
car = Car("Mercedes", 4)

print(vehicle.describe())
print(car.describe())

# 3. Rewrite the `Rectangle` class from #1 as a `@dataclass` instead,
#    keeping `width` and `height` as fields. Note what you get "for free"
#    now vs. what you had to write by hand before (you'll still need to
#    write `area` yourself — dataclasses don't generate methods, only
#    __init__/__repr__/__eq__ from fields).

@dataclass
class Rectangle:
    width: float
    height: float
    
    @property
    def area(self) -> float:
        return self.width * self.height
    
rectangle = Rectangle(3,4)
print(rectangle)
print(rectangle.area)
