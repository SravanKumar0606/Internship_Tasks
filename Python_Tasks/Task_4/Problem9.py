# # Problem 9
# Read a given string, change the character at a given index by inserting a specified character, and then print the modified string.

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)
