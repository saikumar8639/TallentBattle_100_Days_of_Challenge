"""
Day 20 coding Statement : Write a program to identify if the number is Prime number or not

Description

Get a number as input from the user and check whether that number is prime or not.

A prime number is a number with factors as 1 and that number itself.

Input
1
Output
1 is not a prime number

Input
5
Output
5 is a prime number  
"""
#python solution
num=int(input())
f=0
for j in range(2,num):
    if num%j==0:
        f=1
        break
if f==1:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")