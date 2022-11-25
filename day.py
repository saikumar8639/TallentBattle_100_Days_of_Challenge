"""

Day 10 coding Statement:  Write a program to find Factorial of a number
Description
Get a number from user for which you need to fin the factorial, then calculate the factorial and give it as the output.

Input
4

Output
24
"""

number=int(input())
factorial=1
while number:
    factorial*=number
    number-=1
print(factorial)
"""

import math
print(math.factorial(number))

"""