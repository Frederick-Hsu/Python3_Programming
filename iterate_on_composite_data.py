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


print(list(range(10)))
print(list(reversed(range(10))))

x = []
for t in zip(range(-10, 0, 1), range(0, 10, 2), range(1, 10, 2)):
    x += t

print(x)
print(sorted(x))
print(sorted(x, reverse = True))
print(sorted(x, key = abs))

vessels = ["Sloop", "Yawl", "Cutter", "Schooner", "Ketch"]
print(vessels)
print(sorted(vessels, key = str.lower))

temp_list = []
for item in vessels:
    temp_list.append((item.lower(), item))
vessel_list = []
for key, value in sorted(temp_list):
    vessel_list.append(value)

print(vessel_list)

boats = list(zip((1, 3, 1, 3), ("pram", "dory", "kayak", "canoe")))
print(boats)
print(sorted(boats))

def swap(t):
    return t[1], t[0]

print(sorted(boats, key = swap))
print(sorted([3.8, -7.5, 0, 1.3, -6.4, 8.5]))
# print(sorted([3, "spanner", -7.5, 0, 1.3]))     # TypeError: '<' not supported between instances of 'str' and 'int'