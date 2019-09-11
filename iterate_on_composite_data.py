# -*- coding: utf-8 -*-
#
# File name     : iterate_on_composite_data.py
# Description   : Demonstrate how to iterate the composite type of data collection.
# Creator       : Frederique Hsu
# Creation date : Thu.  12 Sep. 2019
# Copyright(C)  2019    All rights reserved.
#

product = 1
i = iter([1, 2, 4, 8])
while True:
    try:
        product *= next(i)
    except StopIteration:
        break

print(product)

# =============================================================================
# product = 1
# for i in [1, 2, 4, 8]:
#     product *= i
# 
# print(product)
# =============================================================================

x = [-2, 9, 7, -4, 3]
print(all(x), any(x), len(x), min(x), max(x), sum(x))
x.append(0)
print(all(x), any(x), len(x), min(x), max(x), sum(x))

for i in range(len(x)):
    x[i] = abs(x[i])

# =============================================================================
# index = 0
# while index < len(x):
#     x[index] = abs(x[index])
#     index += 1
# =============================================================================

# Integer iterator
print("{0}\n{1}\n{2}".format(list(range(5)), 
                             list(range(9, 21)), 
                             tuple(range(10, -25, -5))))
