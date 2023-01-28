"""
Day 71 coding Statement : There are N students in a class, where the i-th student has a score of Ai?.

The i-th student will boast if and only if the number of students scoring less than or equal Ai? is greater than the number of students scoring greater than Ai?.

Find the number of students who will boast.

Input Format

The first line contains T - the number of test cases. Then the test cases follow.
The first line of each test case contains a single integer N - the number of students.
The second line of each test case contains N integers 1,2,…,A1?,A2?,…,AN? - the scores of the students.
Output Format

For each test case, output in a single line the number of students who will boast.

Constraints

1≤10001≤T≤1000
1≤1001≤N≤100
0≤1000≤Ai?≤100
 

Sample Input

3
3
100 100 100
3
2 1 3
4
30 1 30 30

Sample Output

3
2
3
"""
#Python solution

for _ in range(int(input())):
    size=int(input())
    arr=[int(i) for i in input().split()]
    m=0
    c=1
    for i in range(size-1):
        if arr[i]<=arr[i+1]:
            c+=1
        else:
            m=max(c,m)
            c=1
    m=max(c,m)
    print(m)