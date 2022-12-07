"""
Day 22 coding Statement : Write a program to express a number as a sum of two prime numbers

Description

Get a number as input from the user and express that number as sum of two prime numbers.

Input
4

Output
4 can be expressed as sum of 2 and 2

"""
#solution
def isprime(n):
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return False
    return True
num=int(input())
i=2
n=num//2 if num%2==0 else num//2+1
while (i<=n):
    if isprime(i) and isprime(num-i):
        print(num,"can be expressed as sum of",i,"and",num-i)
        break
    i+=1