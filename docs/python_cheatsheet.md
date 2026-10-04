# Python Cheatsheet

## Quick Start

```python
# Variables
name = "AI Engineer"
count = 42

# Functions

def greet(person: str) -> str:
    return f"Hello, {person}!"
```

## Common Data Structures

- `list`: ordered, mutable
- `tuple`: ordered, immutable
- `set`: unordered, unique values
- `dict`: key-value pairs

## Useful Built-ins

```python
nums = [1, 2, 3, 4]
print(len(nums))
print(sum(nums))
print(max(nums))
print(min(nums))
```

## Comprehensions

```python
squares = [n * n for n in range(10)]
```

## Error Handling

```python
try:
    value = int("3")
except ValueError as exc:
    print(f"Invalid conversion: {exc}")
else:
    print("Conversion succeeded")
finally:
    print("This always runs")
```

## OOP Primer

```python
class Person:
    def __init__(self, name: str):
        self.name = name

    def intro(self) -> str:
        return f"Hi, I am {self.name}"
```

## Tips

- Prefer type hints for clarity
- Keep functions focused and small
- Use list/dict comprehensions where they improve readability
- Write tests before or alongside logic changes
