"""

Day 5 coding Statement:  Write a program to identify if the number is even or odd
Description
Get a number as input from the user and check whether the given number is odd or even

Input
10

Output
Even

Input
5

Output
Odd

"""
number=int(input())
if number%2:
    print("Odd")
else:
    print("Even")