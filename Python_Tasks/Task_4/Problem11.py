# # Problem 11
# You are given a string $S$. Your task is to find out if the string contains:
# Alphanumeric characters (isalnum())
# Alphabetical characters (isalpha())
# Digits (isdigit())
# Lowercase characters (islower())
# Uppercase characters (isupper())

s = input()
  
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
