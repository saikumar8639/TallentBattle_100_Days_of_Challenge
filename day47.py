"""
Day 47 coding Statement : Write Program to find longest palindrome in an array
Description
Get an array as the input from the user and find the longest palindrome in that array.

Input
Enter the size of array
3

Enter the elements of array
121 10456 1000001

Output
1000001

"""
size=int(input('Enter the size of array\n'))
arr=[int(i) for i in input("Enter the elements of array\n").split()]
arr=filter(lambda a:str(a)==str(a)[::-1],arr)
print(max(arr))