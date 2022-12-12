"""
Day 27 coding Statement : Write a program to find the double of the given number without using arithmetic operator

Description

For the given input number calculate the double of it without using arithmetic operator.

Input
4

Output
8
"""
# Python solution
numbeer=int(input("Enter a number to double: "))
double=numbeer
for i in range(numbeer):
    double+=1
print("Doubel of",numbeer,"is :",double)