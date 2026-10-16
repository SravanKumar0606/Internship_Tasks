# Problem 5
# Read integers from $1$ to $n$ and print them together as a single string without spaces or string methods.

n=int(input())
s=""
for i in range(1,n+1):
    s=s+str(i)
print(s)
