# 17 Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(input().split())
n = int(input())
print(all(A.issuperset(other := set(input().split())) and len(A) > len(other) for _ in range(n)))
