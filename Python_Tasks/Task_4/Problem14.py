# Problem 14
# Apply your knowledge of the .add() operation to help your friend Rupal. 
# Rupal has a huge collection of country stamps. 
# She decided to count the total number of distinct country stamps in her collection. 
# You pick the stamps one by one from a stack of country stamps. 
# Find the total number of distinct country stamps.

n=int(input())
countries=set()
for i in range(n):
    country=input()
    countries.add(country)
print(len(countries))    
