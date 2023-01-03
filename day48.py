"""
Day 48 coding Statement : Write Program to remove duplicate elements in an array
Description
Get an array as input from the user and then remove all the duplicate elements in that array.

Input

Enter the size of array
5

Enter the elements of array
35 35 45 60 60

Output
35 45 60
"""

size=int(input("Enter the size of array\n"))
arr=[int(i) for i in input("Enter the elements of array\n").split()]
d=[]
for i in arr:
    if str(i) not in d:
        d.append(str(i))
print(" ".join(d))