# -*- coding: utf-8 -*-
#
# File name     : Functions.py
#

import math

def heron(a, b, c):
    s = (a + b + c)/2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def heron2(a, b, c, *, units = "meters"):
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return "{0} square {1}".format(area, units)

print(heron2(25, 24, 7))
print(heron2(41, 9, 40, units = "inches"))
# print(heron2(25, 24, 7, "inches"))    # TypeError: heron2() takes 3 positional arguments but 4 were given

import string
def letter_count(text, letters = string.ascii_letters):
    letters = frozenset(letters)
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count

print("There are {0} letters".format(letter_count("Maggie and Hopey")))
print("There are {0} letters".format(letter_count("Maggie and Hopey", letters = "aeiouAEIOU")))

def shorten(text, length = 25, indicator = "..."):
    '''
    Returns text or a truncated copy with the indicator added,
    
    text is any string; length is the maximum length of the returned string
    (including any indicator); indicator is the string added at the end to 
    indicate that the text has been shortened.
    
    >>> shorten("The Road")
    'The Road'
    >>> shorten("No Country for Old Men", 20)
    'No Country for Ol...'
    >>> shorten("Cities of the Plain", 15, "*")
    'Cities of the *'
    '''
    if len(text) > length:
        text = text[:length-len(indicator)] + indicator
    return text

print(shorten("The Road"))
print(shorten(length = 7, text = "The Road"))
print(shorten("The Road", indicator = "&", length = 7))
print(shorten("The Road", 7, "&"))

# =============================================================================
# def append_if_even(x, lst = []):    # Wrong!
#     if x % 2 == 0:
#         lst.append(x)
#     return lst
# 
# =============================================================================
def append_if_even(number, lst = None):
    if lst is None:
        lst = []
    if number % 2 == 0:
        lst.append(number)
    return lst

# =============================================================================
# def append_if_even(x, lst = None):
#     lst = [] if lst is None else lst
#     if x % 2 == 0:
#         lst.append(x)
#     return lst
# =============================================================================
    
def product(*args):
    result = 1;
    for arg in args:
        result *= arg
    return result

print(product(1, 2, 3, 4))
print(product(5, 3, 8))
print(product(11))

def sum_of_power(*args, power = 1):
    result = 0
    for arg in args:
        result += arg ** power
    return result

print(sum_of_power(1, 3, 5))
print(sum_of_power(1, 3, 5, power = 2))

# Prohibit using positional arguments, but allow keyword arguments
def print_setup(*, paper = "Letter", copies = 1, color = False):
    print("Paper format: {0}".format(paper))
    print("Number of copies: {0}".format(copies))
    print("and enable/disable color? {0}".format(color))

options = dict(paper = "A4", color = True)
print_setup(**options)      # split the dict by introducing the ** mapping splitting operator

def add_person_details(ssn, surname, **kwargs):
    print("SSN = ", ssn)
    print("    surname = ", surname)
    for key in sorted(kwargs):
        print("    {0} = {1}".format(key, kwargs[key]))

add_person_details(83272127, "Luther", forename = "Lexis", age = 47)

def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print("positional argument {0} = {1}".format(i, arg))
    for key in kwargs:
        print("keyword argument {0} = {1}".format(key, kwargs[key]))

