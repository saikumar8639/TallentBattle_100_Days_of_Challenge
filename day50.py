"""
Day 50 coding Statement : Given an integer array of size N. Write Program to find sum of positive square elements in the array.

Sample input 1 :
4 1 2 3 4
Sample output 1 :
30

Explanation :
(1 + 4 + 9 + 16) = 30

Sample input 2 :
4 -1 -2 -3 -4
Sample output 2 :
30

Explanation :
(1 + 4 + 9 + 16) = 30
"""
#Python solution
arr=[int(i) for i in input().split()]
print(sum(list(map(lambda a:a**2,arr[1:]))))