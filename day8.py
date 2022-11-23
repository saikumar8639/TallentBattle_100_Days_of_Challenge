"""
Day 8 coding Statement:  Write a program to find roots of a quadratic equation

Description

Get the values of a, b and c (coefficients of quadratic equation) as input from the user and calculate the roots 
and print as the output.

Input
Enter the value of a, b and c : 1 -6 9

Output
Roots are equal
Root 1= root 2 = 3.00
"""
a,b,c=map(int,input("Enter the value of a, b and c :").split())
root1= (-b + (b**2-(4*a*c))**0.5)/(2*a)
root2= (-b - (b**2-(4*a*c))**0.5)/(2*a)
if root2==root1:
    print("Roots are equal\nRoot 1=Root 2= ",root1)
else:
    print("Roots are different\nRoot 1= ",root1,'Root 2= ',root2)