"""
Day 17 coding Statement : Write a program to find the Factors of a number

Description
Get an input from the user and find the factors of the number.

Input
4

Output
1,2,4  
"""
#Python SOlution
number=int(input())
l=[] #empty list
for i in range(1,number+1):
    if number%i==0:
        l.append(str(i))
print(",".join(l))