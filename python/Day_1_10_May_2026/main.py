# CLP 

# Problem 1 — Largest Number in List
# Goal
# Find maximum value manually without using max().
# Logic
# Assume first element is largest
# Traverse list
# Replace largest when bigger element founds

my_list = [33 , 22 , 55 ,34 , 64 , 21 , 1 , 0]

def find_largest(list):
    largest_num = list[0]
    for i in list :
        if i > largest_num :
            largest_num = i 
    
    return largest_num
    

print("largest number in the list : " , find_largest(my_list))


# Problem 2 — Even/Odd Function
# Goal
# Check whether number divisible by 2.
# Key concept:
# num % 2 == 0

test_num = 22

def even_or_odd(num):
    if num % 2 == 0 :
        print("yes the number is even")
    else :
        print("the number is odd")

even_or_odd(test_num)



# Problem 3 — Loop Through Dictionary
# Goal
# Print all keys and values.
# Use:
# dict.items()

sample_dict = {
    "name" : "Rao Rizwan",
    "age" : 24 ,
    "gender" : "Male"
}

def print_dict(dict):
    for key , value in dict.items():
        print(key , value)
        
print_dict(sample_dict)




# Questions (Easy → Medium)
# Create a list of 5 numbers and print the last element.
list1 = [22 , 12 , 33 , 54 , 21]
print(list1[len(list1) - 1])

# Create a function that returns square of a number.
test_value = 4
def square(num):
    return num*num

print(square(test_value))


# Loop through:
# {"a":1, "b":2, "c":3}
# and print keys only.

dict1 = {"a" : 1 , "b" : 2 , "c" : 3}
for key in dict1:
    print(key)
    
# Count how many even numbers exist in a list.
test_list = [1,2,3,4,6]

def fetch_total_evens(list):
    print(list)
    total_evens = 0
    for i in list :
        print(i)
        if i % 2 == 0 :
            total_evens += 1 
    return total_evens

print("total evens values in the test list are : " , fetch_total_evens(test_list))


# Create a dictionary of students and marks.
# Print only students scoring above 80.

student_marks = {
    'std1' : 90 , 'std2' : 70 ,  'std3' : 40 , 'std4' : 90 , 'std5' : 100 , 'std6' : 70 , 
}

for key , value in student_marks.items():
    if value > 80 :
        print(key)


# Find second largest number in list without sorting.
numbers_list = [10, 4, 80, 56]

def second_largest(numbers_list):
    highest_num = numbers_list[0]
    second_highest_num = numbers_list[1]
    
    for i in numbers_list :
        if i > highest_num :
            highest_num = i 
    
    for j in numbers_list :
        if j == highest_num :
            continue
        if j > second_highest_num :
            second_highest_num = j
    
    print(second_highest_num)
    
second_largest(numbers_list)


# Interview Questions
# Difference between list and tuple?

# list are mutable means its value can be changes while the execultion phase too where as tuple are immutable means it value are unchangable once declared
# tuple uses less memory then list so we prefer tuple when data is immutable and we need more speed


# # Why are dictionaries fast in Python?
# dict are fast in python becuase they are indexed based on keys  , so the lookup becomes really easy 

# # Difference between return and print?
# return is a keyword used to exit from a fuction at any point or condition where as print is just used to show value to the terminal

# # When would you use while instead of for?
# we will use while when we dont know the number of values and we are not sure about number of times a loop will run



# nums = [4, 2, 9, 7, 5]
# Output:
# Largest: 9
# Second Largest: 7
# Even Count: 1

# Conditions:
# single traversal only
# no sorting
# no max()
# no extra loops

nums = [4, 2, 9, 7, 5]
largest = nums[0]
even_counter = 0
sec_largest = nums[0]

for i in nums :
    if i % 2 == 0 :
        even_counter += 1
    if i > largest :
        largest = i
    elif i > sec_largest and i != largest :
        sec_largest = i
        
print("Largest : " , largest)
print("second largest : " , sec_largest)
print("EVEN Count : " , even_counter)