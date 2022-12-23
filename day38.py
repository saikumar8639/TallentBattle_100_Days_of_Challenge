"""
Day 38 coding Statement : Write a Program to print Non-repeating characters in a string

Description

Get a string as the input from the user and print the non-repeating characters in a string.

Input

Hello

Output

H e o

 

To solve the above coding statement, if you need, you can refer to below learning modules.

C Module to Refer: Flow control, Functions, Operators, String

Python Module to refer: Flow control, Functions, Operators, String

C++ Module to Refer: Flow control, Functions, Operators, String

Java Modules to Refer: Flow control, Functions, Operators, String

"""
#take user input
String = "Deepak"

for i in String:
    count = 0
    for j in String:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i,end = " ")