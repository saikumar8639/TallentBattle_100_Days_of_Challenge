"""
Day 52 coding Statement : Given an integer array of size N, write a program to reverse the array;
Sample input 1:
4
2 4 1 3

Sample output 1:
3 1 4 2

Sample input 2:
5
1 5 7 5 3

Sample output 2:
3 5 7 5 1
"""
#Python solution
size=int(input())
arr=[int(i) for i in input().split()]
array=[]
for i in arr:
    array.insert(0,i)
print(array)