# 13 Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem

n=int(input())
roll_numbers_E=set(map(int,input().split()))
b=int(input())
roll_numbers_F=set(map(int,input().split()))
s=roll_numbers_E.union(roll_numbers_F)
print(len(s))
