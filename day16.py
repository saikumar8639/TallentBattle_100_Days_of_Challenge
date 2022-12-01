"""
Day 16 coding Statement : Write a program to identify if the number is Perfect number or not

Description

Get the input from the user and check whether that number is a perfect number or not.

E.g. Let number is 28, factors of 28 are 1,2,4,7,14. Now the sum of all these factors are 28 itself.

Input
28

Output
Perfect Number

Input
4

Output
Not a perfect number 
"""
#Python solution
number=int(input())
c=0
for i in range(1,number):
    if number%i==0:
        c+=i
if c==number:
    print("Perfect Number")
else:
    print("Not a perfect Number")