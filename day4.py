"""

Day 4 coding Statement:  Write a program to identify of the a number is positive or negative

Description


Get an input number from the user and check whether it is a positive or negative number.

Input : -10
Output : Negative number

Input :0
Output : Neither positive nor negative

Input :15
Output : Positive number

"""
input_from_user=int(input())

if input_from_user >0:
    print("Positive Number")
elif input_from_user <0:
    print("Negative number")
else:
    print("Neither positive nor negative")