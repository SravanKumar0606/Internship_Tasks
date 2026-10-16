# Problem 15
# You are given $n$ words. 
# Some words may repeat. 
# For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word.

import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return
        
    # The first line contains the number of words
    n = int(input_data[0].strip())
    
    # Use a standard dictionary (maintains insertion order in Python 3.7+)
    word_counts = {}
    
    # Process the next n lines
    for i in range(1, n + 1):
        if i < len(input_data):
            word = input_data[i].strip()
            if word:
                word_counts[word] = word_counts.get(word, 0) + 1
        
    # Print total number of distinct words
    print(len(word_counts))
    
    # Print the occurrences of each distinct word in order of appearance
    print(*(word_counts.values()))

if __name__ == '__main__':
    solve()
