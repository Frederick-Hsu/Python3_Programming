# -*- coding: utf-8 -*-
#
# File name     : Assertion.py
# Description   : Study the assertion in Python3
# Creator       : Frederick Hsu
# Creation date : Tue.  29 Oct. 2019
# Copyright(C)  2019    All rights reserved.
#

def product(*args):         # pessimistic
    assert all(args), "0 argument"
    result = 1
    for arg in args:
        result *= arg
    return result

# =============================================================================
# def product(*args):         # optimistic
#     result = 1
#     for arg in args:
#         result *= arg
#     assert result, "0 argument"
#     return result
# =============================================================================

print(product(1, 3, 5, 7, 0, 8, 4))