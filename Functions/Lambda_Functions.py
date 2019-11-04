# -*- coding: utf-8 -*-
#
# File name     : Lambda_Functions.py
# Description   : Study the lambda functions in Python3
# Creator       : Frederick Hsu
# Creation date : Tue.  29 Oct. 2019
# Copyright(C)  2019    All rights reserved.
#

s = lambda x: "" if x == 1 else "s"

count = 1
print("{0} file{1} processed".format(count, s(count)))

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
def ignore0(e):
    return e[1], e[2]

elements.sort(key = lambda e: (e[1], e[2]))
print(elements)

# =============================================================================
# elements.sort(key = lambda e: e[1:3])
# print(elements)
# =============================================================================

elements.sort(key = lambda e: (e[2].lower(), e[1]))
print(elements)

area = lambda b, h: 0.5 * b * h
def area(b, h):
    return 0.5 * b * h

print(area(6, 5))

import collections

minus_one_dict = collections.defaultdict(lambda: -1)
point_zero_dict = collections.defaultdict(lambda: (0, 0))
message_dict = collections.defaultdict(lambda: "No message available")
print(minus_one_dict[5])
print(point_zero_dict[9])
print(message_dict[""])