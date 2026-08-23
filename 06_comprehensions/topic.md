# 06 — List / Dict / Set Comprehensions

The single most distinctive piece of everyday Python syntax coming from
JS/PHP. Conceptually it's `.map()`/`.filter()` chains (JS) or
`array_map`/`array_filter` (PHP) — but expressed as an inline expression
instead of a chain of function calls.

## List comprehension

```python
nums = [1, 2, 3, 4, 5]

squares = [n * n for n in nums]
# equivalent to: nums.map(n => n * n) in JS
```

Read it as: `[expression for item in iterable]`.

With a filter:

```python
evens_squared = [n * n for n in nums if n % 2 == 0]
# equivalent to: nums.filter(n => n % 2 === 0).map(n => n * n) in JS
# — but one pass, one expression, no intermediate array
```

`for`/`if` order in the comprehension matches the order you'd write it as
nested code:

```python
[n * n for n in nums if n % 2 == 0]
# is shorthand for:
result = []
for n in nums:
    if n % 2 == 0:
        result.append(n * n)
```

## Nested loops in a comprehension

```python
pairs = [(x, y) for x in range(3) for y in range(2)]
# reads left-to-right same as nested for-loops: outer loop first, inner loop second
```

## Dict comprehension

```python
names = ["alice", "bob"]
lengths = {name: len(name) for name in names}
# {"alice": 5, "bob": 3}
# equivalent to Object.fromEntries(names.map(n => [n, n.length])) in JS
```

## Set comprehension

```python
unique_lengths = {len(name) for name in names}   # {5, 3}
```
Braces like a dict comprehension, but no `:` — that's the only syntactic
difference between set and dict comprehensions.

## Generator expression (bonus: lazy version)

```python
total = sum(n * n for n in nums)   # no brackets at all — lazy, doesn't build a list
```
Use this when you're immediately feeding the result into something like
`sum()`, `max()`, `any()`, `list()` — you don't need the intermediate
collection materialized in memory.

## When to reach for a comprehension vs a plain loop

Comprehensions are idiomatic for simple transform/filter operations — most
experienced Python code prefers them over an equivalent `for` + `.append()`
loop when it fits on one readable line or two. Once the logic needs multiple
statements, side effects, or several conditions, drop back to a normal
`for` loop — a comprehension crammed past readability is a common
Python code-smell, not a badge of honor.
