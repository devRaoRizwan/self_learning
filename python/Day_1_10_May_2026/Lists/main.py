
# list creation 
nums = [11 , 22 , 33 , 44 , 55 , 66 , 77 , 88 ]
print("list : " , nums)

# appending 
nums.append(66)
print("after appending : " , nums)

# removing 
nums.remove(33)
print("list after using remove without giving value in it : " , nums)

# pop 
nums.pop(-3)
print("list after using pop : " , nums)

# sort 
nums.sort()
print('list after sorting : ' , nums)

nums .sort(reverse= True)
print("list after reverse sort aka desc" , nums)

# len
print("lenght of list : ",len(nums))

# max and min 
print("max of list : ",max(nums))
print("min of list : " , min(nums))

list = ["ABC" , "abc" , "Abc"]
print("max of char list : " , min(list))