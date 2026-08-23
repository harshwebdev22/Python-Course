# 07 — Classes: Python vs JS/PHP OOP

Classes, inheritance, encapsulation — same concepts. The mechanics differ
enough to genuinely trip you up, so this one's worth reading closely.

## `self` is explicit and first, always

```python
class Dog:
    def __init__(self, name: str) -> None:   # constructor — always named __init__
        self.name = name

    def bark(self) -> str:                    # `self` must be the first param, every method
        return f"{self.name} says Woof!"
```

JS/PHP's `this` is implicit inside a method. Python's `self` is just a
regular parameter you must declare and name yourself (convention is `self`,
not enforced) — and you access instance attributes via `self.x`, never bare
`x`. When you *call* the method, you don't pass it: `Dog("Rex").bark()` —
Python passes the instance as `self` automatically at call time.

## `__init__`, not `constructor`

```python
d = Dog("Rex")   # no `new` keyword
print(d.bark())
```
No `new`. Instantiation is just calling the class like a function.

## No explicit field declarations — attributes are just assigned in `__init__`

```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
```
Unlike TS/PHP where you often declare `private float $x;` up top, Python
attributes come into existence the moment you assign `self.attr = ...`,
usually in `__init__`. Type hints on attributes are optional and typically
just annotate the `__init__` parameters, as above.

## "Private" is convention, not enforced

```python
class Account:
    def __init__(self, balance: float) -> None:
        self._balance = balance     # leading underscore = "internal, don't touch" (convention)
        self.__secret = "x"         # double leading underscore = name-mangled, harder to access accidentally
```
No `private`/`public`/`protected` keywords. A single leading underscore
signals "internal" to other developers but is fully accessible from outside.
Double-underscore triggers *name mangling* (`_Account__secret`), which
mostly deters accidental access, not determined access. Python trusts you.

## Dunder methods — operator overloading via `__x__` methods

```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:              # controls what print()/debugger shows — like JS's toString()
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:  # controls == — like implementing equals()
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":  # overloads the `+` operator — no equivalent in JS/PHP
        return Point(self.x + other.x, self.y + other.y)
```
Operator overloading (`__add__`, `__len__`, `__getitem__`, etc.) has no
JS/PHP equivalent (PHP forbids it entirely) — this is a genuinely new idiom.
`__repr__`/`__str__` together are Python's `toString()`/`__toString()`.

## Inheritance: parens, not `extends`, and explicit `super().__init__()`

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

class Dog(Animal):                          # base class in parens after the class name
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)               # must call the parent constructor explicitly
        self.breed = breed
```
Python doesn't auto-call the parent's `__init__` for you the way some
languages implicitly chain constructors — you call `super().__init__(...)`
yourself, and only if you actually override `__init__`.

## No interfaces; duck typing (or ABCs) instead

Python has no `interface` keyword. Two common approaches:
- **Duck typing** (default Python style): if an object has the right
  methods, use it — no formal contract needed. "If it walks like a duck and
  quacks like a duck..."
- **`abc.ABC`** (formal, when you actually want an enforced contract):

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...   # subclasses MUST implement this or they can't be instantiated
```

## `@property` — computed attributes accessed like fields, not calls

```python
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14159 * self.radius ** 2

c = Circle(2)
print(c.area)   # note: no parens — accessed like a plain attribute, computed on read
```
Closest equivalent: PHP/JS getters (`__get`/`get area()`), but far more
commonly used in everyday Python classes.

## `@dataclass` — the modern shortcut for plain data-holding classes

Writing `__init__` by hand for a simple data container is boilerplate
Python has a decorator for:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    # __init__, __repr__, and __eq__ are generated for you from the type hints above
```
This is the idiomatic modern replacement for a hand-written "just holds
some fields" class — reach for it before writing `__init__` boilerplate by
hand for data-only classes.
