"""
Day 34 coding Statement : Write a Program to Remove brackets from an algebraic expression

Description

Get an algebraic expression as input from the user and then remove all the brackets in that.

Input
7x+(2*y)

Output
7x+2*y

"""
#Python solution
expression=input()
s=""
for i in expression:
    if i!= '(' and i!=')':
        s+=i
print(s)