"""
Day 45 coding Statement : Write Program to find smallest and largest element in an array
Description
Get an array as input from the user and then find the smallest and largest element in the array.

Input
Enter the size of array :
5
Enter the elements :
10 20 5 40 30

Output
Smallest Number :
5
Largest Number :
40
"""
size=int(input("Enter the size of array :\n"))
array=[int(i) for i in input("Enter the elements :\n").split()]
from math import inf
se=inf
le=-inf
for i in array:
    if se>i:
        se=i 
    if le<i:
        le=i
print("Smallest Number :")
print(se)
print("Largest Number :")
print(le)