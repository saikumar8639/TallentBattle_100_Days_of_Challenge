"""
Day 42 coding Statement : Write Program to check if two arrays are the same or not

Description

Get two arrays as the input from the user and check whether it is the same or not.

Input

Enter the size of first array :
3

Enter the size of second array :
3

Enter elements of first array :
1 2 3

Enter elements of second array :
1 2 3

Output
Same
"""
n1=int(input("Enter the size of first array:\n"))
n2=int(input("Enter the size of second array:\n"))
arr1=sorted([int(i) for i in input("Enter elements of first array :").split()])
arr2=sorted([int(i) for i in input("Enter elements of first array :").split()])
if n1==n2 and arr1==arr2:
    print("Same")
else:
    print("Not same")