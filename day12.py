"""
Day 12 coding Statement:  Write a program to find Sum of digits of a number

Description
Get a number from user and then find the sum of the digits in the given number.

E.g. let the number = 341
Sum of digits is 3+4+1= 8

Input
4521

Output
12

"""
#python solution
number=int(input())
sum_of_num=0
while number:
    sum_of_num+=(number%10)
    number//=10
print(sum_of_num)