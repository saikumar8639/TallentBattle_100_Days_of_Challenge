"""
Day 90 coding Statement : 

Gru has a string S of length N, consisting of only characters a and b for banana and P points to spend.

Now Gru wants to replace and/or re-arrange characters of this given string to get the lexicographically smallest string possible. For this, he can perform the following two operations any number of times.

Swap any two characters in the string. This operation costs 11point. (any two, need not be adjacent)
Replace a character in the string with any other lower case english letter. This operation costs 2 points.
Help Gru in obtaining the lexicographically smallest string possible, by using at most P points.

Input:

First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains two lines of input, first-line containing two integers N , P.
The second line contains a string S consisting of N characters.
Output: For each testcase, output in a single containing the lexicographically smallest string obtained.

 

Sample Input

1

3 3

bba

 

Sample Output

aab
"""

#Python solution