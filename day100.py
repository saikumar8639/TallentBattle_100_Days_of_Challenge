"""
Day 100 coding Statement : 

You have prepared four problems. The difficulty levels of the problems are A1?,A2?,A3?,A4? respectively. A problem set comprises at least two problems and no two problems in a problem set should have the same difficulty level. A problem can belong to at most one problem set. Find the maximum number of problem sets you can create using the four problems.

Input Format

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains four space-separated integers A1?, A2?, A3?, A4?, denoting the difficulty level of four problems.
Output Format

For each test case, print a single line containing one integer - the maximum number of problem sets you can create using the four problems.

 

Sample Input

3

1 4 3 2

4 5 5 5

2 2 2 2

 

Sample Output

2

1

0

"""
#python solution some
 
from collections import Counter
for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=Counter(a)
    a=[]
    for k,v in b.items():
        a.append(v)

    if 4 in a:
        print("0")
    elif 3 in a:
        print("1")
    p=a.count(2)
    q=a.count(1)
    if p==2 or p==1 or q==4:
        print("2")