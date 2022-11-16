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

if s.isalpha():
    if s in ["a","e",'i','o','u','A','E','I','O','U']:
        print("Vowel")
    else:
        print('Consonant')
else:
    print("Invalid Input")