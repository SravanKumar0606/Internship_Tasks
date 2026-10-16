# Problem 20
# There is an array of $n$ integers. 
# There are also 2 disjoint sets, $A$ and $B$, each containing $m$ integers. 
# You like all the integers in set $A$ and dislike all the integers in set $B$. 
# Your initial happiness is $0$.   

def solve():
  
    n, m = map(int, input().split())
    

    arr = list(map(int, input().split()))
 
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    happiness = sum((i in set_a) - (i in set_b) for i in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()
