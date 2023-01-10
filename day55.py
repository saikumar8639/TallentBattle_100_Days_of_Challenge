"""
Day 55 coding Statement : Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the sum of maximum scalar product (Dot product) of 2 vectors.

Sample input 1:
4
1 2 3 4
5 6 7 8

Sample output 1:
70

Explanation :
(8*4 + 7*3 + 6*2 + 1*5) = 70

Sample input 2:
4
-1 -2 -3 -4
5 6 -7 -8

Sample output 2:
37

Explanation :
(-4*-8 + -3*-7 + -2*5 + -1*6) = 37
"""
#Python solution
size=int(input())
arr1=sorted([int(i) for i in input().split()])
arr2=sorted([int(i) for i in input().split()])
s=0
for i in range(size):
    s+=arr1[i]*arr2[i]
print(s)