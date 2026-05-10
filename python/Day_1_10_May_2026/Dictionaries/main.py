
student = {
    "name" : "Rao",
    "age" : 24
}

# reading the value 

stu_age = student["age"]
print(stu_age)

# stu_father = student["father"] 
# print(stu_father)

# to be safe from this we use the get method
""
stu_mother = student.get("mother" , "default_name")
print(stu_mother)



# for looping 
for i , j in student.items():
    print(i , j)

