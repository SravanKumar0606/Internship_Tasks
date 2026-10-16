# Problem 12
# A set is an unordered collection of elements without duplicate entries. 
# When printed, iterated, or converted into a sequence, its elements appear in an arbitrary order. 
# Sets are commonly used for membership testing and eliminating duplicate entries.

def average(array):

    distinct_heights = set(array)

    avg = sum(distinct_heights) / len(distinct_heights)
    
    return round(avg, 3)
