"""
Day 86 coding Statement : 

Mahesh got a beautiful array named A as a birthday gift from his beautiful girlfriend Namratha.
There are N positive integers in that array. Mahesh loved the array so much that he started to spend a lot 
of time on it everyday. One day, he wrote down all possible subsets of the array. Then for each subset,
he calculated the sum of elements in that subset and wrote it down on a paper. Unfortunately, 
Mahesh lost the beautiful array :(. He still has the paper on which he wrote all subset sums. 
Your task is to rebuild beautiful array A and help the couple stay happy :)

Input

The first line of the input contains an integer T denoting the number of test cases. 
First line of each test case contains one integer N, the number of elements in A. 
Second line of each test case contains 2^N integers, the values written on paper

Output

For each test case, output one line with N space separated integers in non-decreasing order.

Sample Input

2
1
0 10
2
0 1 1 2

Sample Output

10
1 1
"""
for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
