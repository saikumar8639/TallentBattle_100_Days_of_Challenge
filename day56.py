"""
Day 56 coding Statement : Write Program to find whether the numbers of an array be made equal

Description

Check whether the numbers of array be made equal or not

For eg, for the following input it should print yes because

50*2*3 , 75*2*2 and 150*2 are equal to 300 in all cases. So array numbers can be made equal

Input
3
50 75 150 

Output
Yes
"""
#Python solution
size=int(input())
arr=[int(i) for i in input().split()]
print("Yes") #every array can be made equal eith the help of lcm of the total array