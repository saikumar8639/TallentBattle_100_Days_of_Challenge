"""
Day 11 coding Statement:  Write a program to find Fibonacci series up to n

Description

Fibonacci series is a special series where nth term is the sum of previous two terms in the series. The series starts with 0 and 1 as the first and second term of the series respectively.

Here you need to get the value for nth term from user and then print Fibonacci series containing n terms.

Input
5
Output
0,1,1,2,3

Input
8
Output
0,1,1,2,3,5,8,13
"""

n=int(input())
l=[]
f0=0;f1=1
for _ in range(n):
    l.append(str(f0))
    f2=f0+f1
    f0=f1 
    f1=f2
print(",".join(l))