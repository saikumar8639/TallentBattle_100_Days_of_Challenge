"""
Day 14 coding Statement : Write a program to reverse a given number

Description

Get an input from the user and the print the reverse of the given number as the output

E.g. let the number be 324 then the reverse of the number is 423

Input
675

Output
576
"""
number=int(input())
print("number is :",number)
r_number=int(str(number)[::-1])
print("Reversed number is:",r_number)