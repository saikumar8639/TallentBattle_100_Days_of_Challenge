"""
Day 82 coding Statement : 

You are given N binary strings of length N each. You need to find a binary string of length N which is different from all of the given strings.

Note:

A binary string is defined as a string consisting only of '0' and '1'.
A string is considered different from another string when they have different lengths, or when they differ in at least one position.
Input Format

The first line will contain T - the number of test cases. Then the test cases follow.
The first line of each test case contains N - the number of strings and length of strings.
Each of the next N lines contains a binary string of length N.
Output Format

For each test case, print on one line a binary string of length N, which is different from all of the given strings. If there are multiple possible answers, print any.

 

Sample Input

2

3

101

110

100

4

1100

1010

0100

0010

 

Sample Output

111

1101
"""
#Python solution
for _ in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())