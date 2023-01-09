"""
Day 54 coding Statement : Given an integer array of size N. Write Program to find whether Arrays are disjoint or not. Two arrays are said to be disjoint if they have no elements in common.

Sample input 1:
4
2 -4 -1 -3
3
1 3 5
Sample output 1:
Disjoint

Sample input 2
5
1 5 -7 6 3
4
2 4 6 8
Sample output 2:
Not disjoint. ( 6 is common)
"""
size1=int(input("Enter size of array 1\n"))
arr1={int(i) for i in input("Enter array 1\n").split()}

size2=int(input("Enter size of array 2\n"))
arr2={int(i) for i in input("Enter array 2\n").split()}

if not (len(arr1.intersection(arr2))):
    print("Disjoint")
else:
    print("Not disjoint")