# SimpleUtils

A small Python utility package with basic helper functions.

## 📦 Description

This package provides lightweight and easy-to-use functions for basic operations, including:

- `add_one(number)`: Increment a number by 1.
- `count_in_list(lst, el)`: Count the number of times an element appears in a list.

## 🧰 Functions

### `add_one(number) -> number`

Increments the given numeric value by one.

**Parameters:**
- `number`: An integer or float.

**Returns:**
- `number + 1`

**Example:**
```python
from simpleutils import add_one

print(add_one(4))  # Output: 5
```

## `count_in_list(lst, el) -> int`

Counts how many times el appears in lst.

**Parameters:**

- `lst`: A list.

- `el`: An element to count in the list.

**Returns:**

- `Integer count of el in lst.`

**Example:**
```python
from simpleutils import count_in_list

print(count_in_list([1, 2, 2, 3], 2))  # Output: 2
```

## ✅ Requirements

Python 3.10+

No external dependencies.

## 📁 Installation

To install the package, use one of the following commands:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## 🧪 Testing


Each test is a standalone Python script that can be run individually.
To run them all, you can use:

```bash
python3 tests/test_add_one.py
python3 tests/test_count_in_list.py
```

Or use a shell loop to run them all at once:

```bash
for f in tests/test_*.py; do python3 "$f"; done
```

## 📄 License

MIT License

## ✨ Author

eagle – eagle@42.fr


