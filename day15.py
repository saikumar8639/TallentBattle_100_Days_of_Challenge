"""
Day 15 coding Statement : Write a program to identify if the number is Strong number or not

Description

Get a number as input from user and then check whether that number is a strong number or not. A number is said to be strong number if the sum of the factorial of each digit in the number is same as that of the number.

E.g. let the number be 145

Here 1! + 4! + 5! is 1 + 24 + 120 which is equal to 145 itself.

Input
121

Output
Not a strong number

Input
2

Output
Strong number
"""
#Python solution
import math as m
num=int(input())
n=num
c=0
while n:
    c+=m.factorial(n%10)
    n//=10
if num==c:
    print("Strong number")
else:
    print("Not a strong number")