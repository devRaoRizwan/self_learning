# Core Python Revision — Coding Logic Problems (CLP)

**Date:** Wednesday, 10 May 2026 | Part of the [Core Python Revision](#) series

---

## What is CLP?

After going through the theory of lists and dictionaries, I moved into actual problem solving. The idea behind CLP (Coding Logic Problems) is simple — stop reading, start writing. These problems cover the concepts I just studied but force me to apply them without relying on built-ins as a crutch.

---

## Problems

### Problem 1 — Find the Largest Number in a List

**Goal:** Find the maximum value manually — no `max()` allowed.

**Logic:**
- Assume the first element is the largest
- Traverse the list
- Replace whenever a bigger value is found

```python
my_list = [33, 22, 55, 34, 64, 21, 1, 0]

def find_largest(list):
    largest_num = list[0]
    for i in list:
        if i > largest_num:
            largest_num = i
    return largest_num

print("Largest number in the list:", find_largest(my_list))
# Output: 64
```

---

### Problem 2 — Even or Odd

**Goal:** Check whether a number is divisible by 2.

**Key concept:** `num % 2 == 0` means even.

```python
def even_or_odd(num):
    if num % 2 == 0:
        print("yes the number is even")
    else:
        print("the number is odd")

even_or_odd(22)   # yes the number is even
even_or_odd(7)    # the number is odd
```

---

### Problem 3 — Loop Through a Dictionary

**Goal:** Print all keys and values from a dictionary.

**Key concept:** `.items()` gives you both key and value in each iteration.

```python
sample_dict = {
    "name": "Rao Rizwan",
    "age": 24,
    "gender": "Male"
}

def print_dict(dict):
    for key, value in dict.items():
        print(key, value)

print_dict(sample_dict)
```

---

## Practice Questions (Easy → Medium)

**Print the last element of a list without hardcoding the index:**

```python
list1 = [22, 12, 33, 54, 21]
print(list1[len(list1) - 1])   # 21
```

**Function that returns the square of a number:**

```python
def square(num):
    return num * num

print(square(4))   # 16
```

**Loop through a dictionary and print keys only:**

```python
dict1 = {"a": 1, "b": 2, "c": 3}
for key in dict1:
    print(key)
```

**Count how many even numbers exist in a list:**

```python
def fetch_total_evens(list):
    total_evens = 0
    for i in list:
        if i % 2 == 0:
            total_evens += 1
    return total_evens

print("Total even values:", fetch_total_evens([1, 2, 3, 4, 6]))   # 3
```

**Print only students scoring above 80:**

```python
student_marks = {
    'std1': 90, 'std2': 70, 'std3': 40,
    'std4': 90, 'std5': 100, 'std6': 70
}

for key, value in student_marks.items():
    if value > 80:
        print(key)
# std1, std4, std5
```

**Find the second largest number without sorting:**

```python
def second_largest(numbers_list):
    highest_num = numbers_list[0]
    second_highest_num = numbers_list[1]

    for i in numbers_list:
        if i > highest_num:
            highest_num = i

    for j in numbers_list:
        if j == highest_num:
            continue
        if j > second_highest_num:
            second_highest_num = j

    print(second_highest_num)

second_largest([10, 4, 80, 56])   # 56
```

---

## Interview Questions

**Difference between list and tuple?**

Lists are mutable — their values can be changed even after they're created. Tuples are immutable — once declared, the values are locked. Tuples also use less memory, so when data doesn't need to change, tuples are the faster and lighter choice.

**Why are dictionaries fast in Python?**

Because they're indexed by keys using hashing. Python doesn't scan through everything — it computes a hash for the key and goes directly to the value. Average lookup time is O(1).

**Difference between `return` and `print`?**

`print` just displays something to the terminal — it has no effect on the function's behavior. `return` actually exits the function and passes a value back to wherever it was called from. In real code, you almost always want `return`.

**When would you use `while` instead of `for`?**

When you don't know in advance how many times the loop needs to run. A `for` loop is for when you have a defined sequence to iterate over. A `while` loop runs as long as a condition is true — useful for things like user input, retries, or game loops.

---

## Challenge Problem — Single Traversal

**Constraints:** single loop only, no sorting, no `max()`, no extra loops.

**Task:** From `nums = [4, 2, 9, 7, 5]`, find the largest, second largest, and count of even numbers.

```python
nums = [4, 2, 9, 7, 5]
largest = nums[0]
sec_largest = nums[0]
even_counter = 0

for i in nums:
    if i % 2 == 0:
        even_counter += 1
    if i > largest:
        largest = i
    elif i > sec_largest and i != largest:
        sec_largest = i

print("Largest:", largest)          # 9
print("Second Largest:", sec_largest)  # 7
print("Even Count:", even_counter)  # 1
```

This one was interesting — you have to track three things in a single pass, which means the order of your conditions actually matters.

---

*This is part of my ongoing Core Python Revision series — problems I'm solving as I go, written the way I actually think through them.*