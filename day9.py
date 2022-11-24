"""

Day 9 coding Statement : Write a program to find Number of digits in an integer

Description

Take an integer as the input from the user and then calculate the number of digits in the given input and print it as the output.

Input
3241
Output
4 

Input
6
Output
1
"""
number=int(input())
print(len(str(number))) #len is used to find the length
# str is used to convert int to string 