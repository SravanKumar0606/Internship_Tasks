# 18 Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

input()
A = set(map(int, input().split()))
for _ in range(int(input())):
    op, _ = input().split()
    other_set = set(map(int, input().split()))
    getattr(A, op)(other_set)
print(sum(A))
