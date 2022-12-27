"""
Day 40 coding Statement : Write a Program to Replace substring in a string

Description
Get a string as input from the user and then get another string which has to be removed from the string.
Get the third input, the new substring which is placed in that substring position.
Finally print the output by replacing the substring with new string.

Input
Enter a string
talentbattle

Enter the substring to be removed :
talent

Enter the new substring :
student

Output

The new string :
studentbattle
"""
string=input("Enter a string:\n")
substr1=input("Enter the substring to be removed :\n")
substr2=input("Enter the new substring:\n")
print("The new string :\n"+str(string.replace(substr1,substr2)))