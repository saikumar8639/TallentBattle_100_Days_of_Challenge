"""
Day 51 coding Statement : Given an integer array of size N, write a program to sort the array;

Sample input 1:
4 2 4 1 3

Sample output 1:
1 2 3 4

Sample input 2:
5 1 5 7 5 3

Sample output 2:
1 3 5 5 7

"""
arr=[int(i) for i in input().split()]
arr=arr[1:]
for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if (arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in arr:
    print(i,end=" ")