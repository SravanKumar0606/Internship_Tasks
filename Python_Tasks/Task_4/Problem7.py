# Problem 7
# Write a Python function split_and_join(line) that splits the string on a space (" ") delimiter and joins the words using a hyphen ("-").

def split_and_join(line):
    return "-".join(line.split(" "))
