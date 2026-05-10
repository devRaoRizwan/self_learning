# Core Python Revision — Dictionaries

**Date:** Wednesday, 10 May 2026 | Part of the [Core Python Revision](#) series

---

## What is a Dictionary?

A dictionary (or just `dict`) is a collection that stores data as **key-value pairs**. Instead of accessing values by a numbered index like lists, you access them by a meaningful key — which makes lookups fast and the data easy to read.

```python
dict_name = {
    "name": "Rao",
    "age": 24
}
```

Why dictionaries matter:

- **Fast lookup** — finding a value is quick because of how Python implements them internally (hashing, more on that below).
- **Structured data** — great for representing real-world objects like a user profile, a config file, or an API response.
- **Widely used** — if you've worked with any API or backend system, you've seen dictionaries everywhere.

---

## Accessing a Value

You access a value using its key:

```python
dict_name["name"]   # returns "Rao"
dict_name["age"]    # returns 24
```

But if you accidentally type a key that doesn't exist:

```python
dict_name["email"]  # ❌ KeyError: 'email'
```

---

## `.get()` — The Safer Way to Access

To avoid `KeyError` and handle missing keys gracefully, use `.get()`:

```python
dict_name.get("name")       # returns "Rao"
dict_name.get("email")      # returns None (no crash)
```

You can also set a **default value** if the key isn't found — which is cleaner than getting `None`:

```python
dict_name.get("email", "not provided")   # returns "not provided"
```

This is what proper exception handling looks like for dictionary access.

---

## Updating a Value

To change the value of an existing key, just reassign it:

```python
dict_name["age"] = 25
# age is now 25
```

---

## Fetching Keys and Values

```python
dict_name.keys()     # returns all keys
dict_name.values()   # returns all values
```

---

## Looping Over a Dictionary

To iterate over every key-value pair, use `.items()`:

```python
for key, value in dict_name.items():
    print(key, value)
```

This is probably the most common pattern you'll use when working with dicts in real code.

---

## `len()`, `max()`, `min()`, `sorted()`

Just like lists, dictionaries support these built-ins — but they operate on the **keys** by default:

```python
len(dict_name)          # number of key-value pairs
max(dict_name)          # largest key (alphabetically or numerically)
min(dict_name)          # smallest key
sorted(dict_name)       # returns a sorted list of keys
```

---

## Why Dictionaries Are Fast — Hashing

Under the hood, Python uses a technique called **hashing** to store and find keys. Instead of scanning through every element one by one, it computes a hash (basically a shortcut address) for each key. This is why:

- Keys **must be immutable** — strings, numbers, tuples work. Lists don't, because they can change and that would break the hash.
- Lookup time is **O(1) on average** — it doesn't matter if your dict has 5 keys or 5 million, finding a value takes roughly the same time.

This is exactly why dictionaries come up so often in DSA and coding interviews.

---

## Quick Reference

| Operation | Syntax | Notes |
|---|---|---|
| Create | `d = {"key": value}` | — |
| Access | `d["key"]` | Raises `KeyError` if missing |
| Safe access | `d.get("key")` | Returns `None` if missing |
| Safe with default | `d.get("key", default)` | Returns default if missing |
| Update | `d["key"] = new_value` | — |
| All keys | `d.keys()` | — |
| All values | `d.values()` | — |
| Loop | `for k, v in d.items()` | Most common pattern |
| Length | `len(d)` | — |
| Sort keys | `sorted(d)` | Returns a list |

---

*This is part of my ongoing Core Python Revision series — written the way I actually understand things, not copy-pasted from docs.*