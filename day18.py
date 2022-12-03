"""
Day 18 coding Statement : Write a program to Add two fractions

Description
Get the values for numerator and denominator of two fractions, then add that fractions. Consider the following format

x3/y3 = (x1/y1) + (x2/y2)

here x3 = (x1*y2) + (x2*y1) and y3 = (y1*y2)

Input
2  3
4  3

Output
2/1   
"""
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
s=(x1/y1+x2/y2).as_integer_ratio()
print(str(s[0])+"/"+str(s[1]))