"""
Day 70 coding Statement : Given an array, rotate the array by one position in clock-wise direction.

Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}

Output:
5 1 2 3 4

Example 2:

Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}

Output:
3 9 8 7 6 4 2 1
"""
N=int(input())
A=[int(i) for i in input().split()]
ans=[]
ans.append(A[-1])
ans+=A[:-1]
for i in ans :
    print(i,end=" ")