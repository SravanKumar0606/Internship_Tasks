# Problem 19
# A shoe shop owner has $X$ number of shoes and a list containing the size of each shoe in his shop. 
# There are $N$ customers willing to pay a certain amount of money ($x$) only if they receive a shoe of their desired size.

from collections import Counter

def solve_shoe_shop():

    num_shoes = int(input())
    
  
    shoe_sizes = list(map(int, input().split()))
    inventory = Counter(shoe_sizes)
    

    num_customers = int(input())
    
    total_earned = 0
    

    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        if inventory[size] > 0:
            total_earned += price
            inventory[size] -= 1
          
    print(total_earned)

if __name__ == '__main__':
    solve_shoe_shop()
