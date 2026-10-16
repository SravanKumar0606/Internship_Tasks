# Problem 13
# Problem Description:Given two sets of integers, M and N,
# print their symmetric difference in ascending order. 
# The symmetric difference of two sets contains those elements that exist in either set M or set N, but not in both.

m = int(input())
set_a = set(map(int, input().split()))

n = int(input())
set_b = set(map(int, input().split()))

symmetric_diff = set_a.symmetric_difference(set_b)

for num in sorted(symmetric_diff):
    print(num)
