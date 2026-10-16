# Problem 6
# The solution sorts unique scores in descending order and prints the second element (arr[1]).

    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort(reverse=True)
    print(arr[1])
