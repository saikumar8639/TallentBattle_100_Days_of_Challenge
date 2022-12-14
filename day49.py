"""
Day 49 coding Statement : Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the minimum scalar product (Dot product) of 2 vectors.

Sample input 1 :
4 1 2 3 4 5 6 7 8
Sample output 1 :
60
Explanation :
(4*5 + 3*6 + 2*7 + 1*8) = 60

Sample input 2 :
4 -1 -2 -3 -4 5 6 -7 -8
Sample output 2 :
-17
Explanation :
(-1*-8 + -2*-7 + -3*6 + -4*5) = -17
"""
#Python solution
arr=[int(i) for i in input().split()]
x=sorted(arr[1:arr[0]+1],reverse=True)
y=sorted(arr[arr[0]+1:])
print(sum([x[i]*y[i] for i in range(arr[0])]))