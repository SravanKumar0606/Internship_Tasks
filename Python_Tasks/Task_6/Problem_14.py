# 20 Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

n1 = int(input())
set1 = set(map(int, input().split()))
n2 = int(input())
set2 = set(map(int, input().split()))
print(len(set1.intersection(set2)))
