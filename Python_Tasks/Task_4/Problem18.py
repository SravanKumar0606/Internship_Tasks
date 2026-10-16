# Problem 18
# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        
        if cmd == 'insert':
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            e = int(command[1])
            lst.remove(e)
        elif cmd == 'append':
            e = int(command[1])
            lst.append(e)
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
