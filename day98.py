"""
Day 98 coding Statement : 

There are N breakfasts in the restaurant “Fat Hut” where the Arun works. The ith breakfast has an attractiveness Ai? and cost Ci?.

Arun has noticed that nobody takes the jth breakfast if there exists at least one breakfast i such that Ai?≥Aj? and Ci?<Cj?.

In other words, if a breakfast is less attractive and more expensive than any of the other dishes, then nobody is interested in that breakfast.

Arun will be happy if all the N breakfasts have a chance to be taken. Unfortunately, Arun has no power over prices. On the other hand, he can change the attractiveness of some breakfasts by some real number. However, after the changes, the attractiveness of the ith breakfast must lie in the interval [Li?,Ri?].

He would also like to change the attractiveness of the minimum number of breakfasts. Help the Chef do it.

Input Format

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
Each testcase contains N+1 lines of input.
The first line of each test case contains a single integer N - number of breakfasts.
N lines follow. For each valid i, the hith of these lines contains four space-separated integers Ai?, Ci?, Li?, Ri? - current attractiveness, cost, the minimal and maximal allowed attractiveness after change of i-th breakfast.
Output Format

For each test case, print in a single line containing one integer - minimum number of breakfasts the Chef should change so that all the N breakfasts have a chance to be taken. Print "-1"(without quotes) if it is impossible to achieve the goal.

 

Sample Input

2

4

5 1 1 5

4 4 2 5

2 2 2 5

3 3 2 5

4

5 1 2 5

4 4 2 5

2 2 2 5

3 3 2 5

 

Sample Output

1

2
"""