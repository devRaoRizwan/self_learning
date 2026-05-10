# Core Python Revision — Lists

**Date:** Wednesday, 10 May 2026

---

## What is a List?

A list is an **ordered, mutable collection** in Python. Here's what that means in plain terms:

- **Ordered** — it remembers the order you put things in. Whatever sequence you insert values, that's how they stay.
- **Mutable** — you can change it after creating it (add, remove, modify).
- **Allows duplicates** — same value can appear more than once.
- **Zero-indexed** — counting starts from `0`, not `1`.

---

## Creating a List

```python
list_name = [value, value, value]

nums = [22, 11, 44]
```

---

## Accessing an Element

You access an element by its index position:

```python
print(nums[0])   # prints 22 (first element)
print(nums[1])   # prints 11
print(nums[2])   # prints 44
```

---

## Modifying an Existing Element

Say we have `nums = [22, 11, 44]` and we want to replace `11` with `55`.

First, find the index — `11` is at index `1`. Then just reassign:

```python
nums[1] = 55
# nums is now [22, 55, 44]
```

---

## Common List Methods

### `append()`

Adds a value to the **end** of the list (the last index).

```python
nums.append(66)
# nums goes from [22, 11, 44] → [22, 11, 44, 66]
```

---

### `remove()`

Removes a value from the list by its **value**, not index. A couple of things to watch out for:

```python
nums.remove()          # ❌ Error: requires exactly one argument
nums.remove(999)       # ❌ Error: list.remove(x): x not in list
nums.remove(11)        # ✅ removes 11 from the list
```

Always make sure the value actually exists in the list before calling `remove()`.

---

### `pop()`

Removes an element by its **index**.

```python
nums.pop()       # removes the last element (index n-1)
nums.pop(1)      # removes element at index 1
nums.pop(99)     # ❌ IndexError: pop index out of range
```

Negative indexing works too — it counts from the end:

```python
lst = [1, 2, 4]
lst.pop(-1)
# -1 means index (length - 1) = 3 - 1 = 2, so 4 gets removed
# lst is now [1, 2]
```

---

### `sort()`

Sorts the list in place. By default it's **ascending**:

```python
lst = [22, 11, 44, 33]
lst.sort()
# result: [11, 22, 33, 44]
```

To sort in **descending** order, set the `reverse` parameter to `True` (it's `False` by default):

```python
lst.sort(reverse=True)
# result: [44, 33, 22, 11]
```

---

### `len()`

Short for *length* — tells you how many elements are in the list:

```python
len(nums)   # returns a number, e.g. 3
```

---

### `max()` and `min()`

These find the largest and smallest values in a list. For numbers it's straightforward. For strings, Python compares using **ASCII/Unicode values**:

```python
lst = ["ABC", "abc", "Abc"]
max(lst)    # returns "abc" (lowercase has higher ASCII value)
min(lst)    # returns "ABC"
```

---

## Quick Reference Table

| Method | What it does |
|---|---|
| `append(val)` | Adds value to the end |
| `remove(val)` | Removes first occurrence of value |
| `pop(index)` | Removes element at given index (default: last) |
| `sort()` | Sorts ascending; use `reverse=True` for descending |
| `len(list)` | Returns number of elements |
| `max(list)` | Returns largest value |
| `min(list)` | Returns smallest value |

---

*This is part of my ongoing Core Python Revision series. I'm documenting concepts as I learn and revisit them — written the way I actually understand things, not the way textbooks explain them.*