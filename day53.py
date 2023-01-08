"""
Day 53 coding Statement : Given an integer array of size N. Write Program to find maximum product subarray in a given array.
Sample input 1:
4
2 -4 -1 -3
Sample output 1:
8 = {2, -4, -1}

Sample input 2:
5
1 5 -7 5 3
Sample output 2:
15 = {5, 3}
"""
#Python solution
size=int(input())
arr=[int(i) for i in input().split()]
arr1=arr[::-1]
for i in range(1,size):
    arr[i]*=arr[i-1] or 1
    arr1[i]*=arr1[i-1] or 1
print(max(arr+arr1))