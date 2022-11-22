"""
Day 7 coding Statement:  Write a program to find Number of days in a given month of a given year

Description

Get the number of month and year as input from the user and check the number of days present in that month.

Input
Enter month : 2
Enter year : 2000

Output
29
"""
from calendar import monthrange
mon=int(input("Enter month : "))
year=int(input("Enter year : "))

print(monthrange(year, mon)[1]) #by using monthrange function we can get no of days in a month