# 1 Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem

n=int(input())
if n%2!=0:
    print("Weird")
if n%2==0:
    if n>=2 and n<=5:
        print("Not Weird")
if n%2==0:
    if n>=6 and n<=20:
        print("Weird")
if n%2==0:
    if n>20:
        print("Not Weird")  
