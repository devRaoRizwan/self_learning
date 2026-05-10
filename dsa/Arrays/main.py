# Problem

# Find largest element in array.

# brute force solution
# we will first of all convert the array in sorted and thent the last one is the largest 
arr = [12 , 21 , 44 , 55 , 66 , -3 , 0 , -21 , -77]
arr.sort()
print("the largest element is : " , arr[-1])
# its time complexity is 0log n as it checks each value and put the smallest to front , means it have to arrnage all 

# Optimal Approach 
# we will think first element is largest and make it compare to all the elements of the array making its time complexity to 0(n)

largest_num = arr[0]
for i in arr :
    if i > largest_num :
        largest_num = i

print("the optimal solution of this and largest value is : " , largest_num)
