"""
Day 37 coding Statement : Write a Program to calculate the Frequency of characters in a string

Description

Get a string as the input from the user and find the frequency of characters in the string.

Input

program

Output

The frequency of a is 1

The frequency of g is 1

The frequency of m is 1

The frequency of o is 1

The frequency of p is 1

The frequency of r is 2
"""
#Python solution
string=input()
from collections import Counter as co
s_count=sorted(co(string))
for i in s_count:
    print("The frequency of",i,"is",co(string)[i])