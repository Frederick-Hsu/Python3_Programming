# -*- coding: UTF-8 -*-
# 
# File name     : yield_fn.py
# Description   : how to get a yield-function.
#
#

# Build and return a list
def letter_range(a, z):
    result = []
    while ord(a) < ord(z):
        result.append(a)
        a = chr(ord(a) + 1)
    return result

# Return each value on demand
def Letter_Range(a, z):
    while ord(a) < ord(z):
        yield a
        a = chr(ord(a) + 1)


if __name__ == "__main__":
    for letter in letter_range("m", "v"):
        print(letter)
    
    letters = letter_range("m", "v")
    print(letters)

    LETTERS = list(Letter_Range("M", "V"))
    print(LETTERS)