"""
Day 36 coding Statement : Write a Program to Capitalize the first and last letter of each word of a string

Description

Get a string from the user and then change the first and last letter to uppercase.

Input

programming

Output

ProgramminG
"""

string=input()
string=string[0].upper()+string[1:-1]+string[-1].upper()
print(string)