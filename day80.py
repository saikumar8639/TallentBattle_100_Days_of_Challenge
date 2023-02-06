"""
Day 80 coding Statement : 

Alice and Bob went to a pet store. There are N animals in the store where the ith animal is of type Ai?.

Alice decides to buy some of these N animals. Bob decides that he will buy all the animals left in the store after Alice has made the purchase.

Find out whether it is possible that Alice and Bob end up with exactly same multiset of animals.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer N — the number of animals in the store.
The next line contains N space separated integers, denoting the type of each animal.
Output Format

For each test case, output on a new line, YES, if it is possible that Alice and Bob end up with exactly same multiset of animals and NO otherwise.

You may print each character in uppercase or lowercase. For example, the strings YES, yes, Yes, and yES are considered identical.

 

Sample Input

4
3
4 4 4
4
2 3 3 2
4
1 2 2 3
6
5 5 1 5 1 5


Sample Output

NO
YES
NO
YES"""
for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    from collections import Counter as c
    arr=c(arr)
    if (all(arr[i]%2==0 for i in arr)):
        print("YES")
    else:
        print("NO")