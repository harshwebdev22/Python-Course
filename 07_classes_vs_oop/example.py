"""Run me: python3 example.py"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Dog:
    def __init__(self, name: str) -> None:  # constructor
        self.name = name

    def bark(self) -> str:
        return f"{self.name} says Woof!"


d = Dog("Rex")  # no `new`
print(d.bark())


class Account:
    def __init__(self, balance: float) -> None:
        self._balance = balance  # "internal" by convention only
        self.__secret = "shh"  # name-mangled

    def deposit(self, amount: float) -> None:
        self._balance += amount


acct = Account(100)
acct.deposit(50)
print(acct._balance)  # accessible anyway — Python trusts you
print(acct._Account__secret)  # mangled name, still reachable if you really want it


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:  # powers print() / debugger display
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":  # operator overloading
        return Point(self.x + other.x, self.y + other.y)


p1, p2 = Point(1, 2), Point(3, 4)
print(p1 + p2)  # -> Point(4, 6), via __add__
print(p1 == Point(1, 2))  # -> True, via __eq__


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Cat(Animal):  # base class in parens
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)  # explicit parent constructor call
        self.breed = breed

    def bark(self) -> str:
        return f"{self.name} the {self.breed} says Meow (not Woof)"


print(Cat("Whiskers", "tabby").bark())


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


print(Square(4).area())
# Shape()  # would raise TypeError — can't instantiate an ABC directly


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:  # accessed without parens, computed each time
        return 3.14159 * self.radius**2


c = Circle(2)
print(c.area)  # no () — looks like a field access


@dataclass
class Vec2:
    x: float
    y: float
    # __init__, __repr__, __eq__ generated for free from the annotations above


v = Vec2(1, 2)
print(v)  # -> Vec2(x=1, y=2), auto-generated __repr__
print(v == Vec2(1, 2))  # -> True, auto-generated __eq__
