"""
Day 39 coding Statement : Write a Program to check if two strings are Anagram or not

Description

Get two strings as input from the user and check whether it is Anagram or not.

Input

sunlight thgiluns

Output

Anagram
"""
#python solution

s1,s2=input("Enter the two strings: ").split()
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")
