"""
Day 44 coding Statement : Write Program to find number of even and odd elements in an array
Description
Get an array as input from the user and then count the number of even and odd elements present in the array.
Input

Enter size of array
4

Enter the elements :
1 3 4 5

Output

Number of even elements :
1

Number of odd elements :
3
"""
#Python solution
size=int(input("Enter size of array \n"))
arr=[int(i) for i in input("Enter the elements :\n").split()]
ee=0
oe=0
for i in arr:
    if i%2==0:ee+=1
    else:oe+=1
print("Number of even elements :\n".ee)
print("Number of odd elements :\n".oe)