#Practice Statement: Write a program to print "Welcome to Talent Battle" on the output screen.

print("Welcome to the Talent Battle")

"""
Day 1 coding Statement: Write a program to identify if the character is a vowel or consonant.
Description of the program: 
Take an input character from the user and check whether the given input is a vowel or consonant.

Test Case 1:
Input
A
Output
Vowel

Test Case 2:
Input
m
Output
Consonant

Test Case 3:
Input
3
Output
Invalid Input

"""

s=input()
from string import ascii_lowercase as low
from string import ascii_uppercase as upp

if s in low:
    print("")
