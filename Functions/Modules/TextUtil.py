#!/usr/bin/env python3
# Copyright(C)  2019    Frederick Hsu,  All rights reserved.
'''
This module provides a few string manipulation functions.

>>> is_balanced("(Python  (is (not (lisp))))")
True
>>> simplify("some     text      with spurious whitespace ")
'some text with spurious whitespace'
'''

import string

def simplify(text, whitespace = string.whitespace, delete = ""):
    '''
    Returns the text with multiple spaces reduced to single spaces
    
    The whitespace parameter is a string of characters, each of which is 
    considered to be a space.
    If delete is not empty, it should be a string, in which case any 
    characters in the delete string are excluded from the resultant string.
    
    >>> simplify("this    and  that  too")
    'this and that too'
    >>> simplify("   Washington    D.C.")
    'Washington D.C.'
    >>> simplify("   Washington          D.C.", delete = ", ;:.")
    'WashingtonDC'
    >>> simplify("disemvoweied ", delete = "aeiou")
    'dsmvwd'
    '''
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)
    return " ".join(result)

def is_balanced(text, brackets = "()[]{}<>"):
    '''
    Check whether the open brackets and close brackets matched well.
    
    Inspect a text string, if there existed some brackets like (), [], {} or <>
    check whether they have open-close matched.
    
    >>> is_balanced("(Python (is [not {lisp}]))")
    True
    >>> is_balanced("This number is smaller (<) than that one", brackets = "()<>")
    False
    '''
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())


#==============================================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()