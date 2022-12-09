"""
Day 24 coding Statement : Write a program to print Pyramid pattern using stars

Description

Get the number of lines as the input and print stars in that many lines or rows in a pyramid shape.

Input

4

Output

  *

 ***

*****

*******
"""
n=int(input())
for i in range(n):
    print(" "*(n-i),"*"*(2*i+1),)
