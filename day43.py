"""
Day 43 coding Statement : Write Program to find the array type

Description

Get an array as input from the user and check the type of the array, whether it is odd, even or mixed type.

Input

Enter size of array :
3

Enter elements 
1 3 5

Output
Odd
"""

size=int(input("Enter size of array :"))
array=[int(i) for i in input("Enter elements\n").split()]
ee=0
oe=0
for i in array:
    if i%2==0:ee=1
    else:oe=1
if ee==0 and oe==1:
    print("odd")
elif ee!=0 and oe==1:
    print("even")   
else:
    print("mixed process")