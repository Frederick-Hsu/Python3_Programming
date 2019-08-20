# -*- coding: utf-8 -*-
#
# File name     : tuples.py
# Description   : Study the subject of tuple type.
# Creator       : Frederick Hsu
# Creation date : Tue.  20 Aug. 2019
# Copyright(C)  2019    All rights reserved.
#


tpl = ("venus", -28, "green", '21', 19.74)
print(type(tpl))
print(tpl)

hair = "black", "brown", "blonde", "red"
print(hair[2])
print(hair[-3:])

hairs = hair[:2], "gray", hair[2:]
print(hairs)

hair_single_tuple = hair[:2] + ("gray",) + hair[2:]     # MUST use both "()" and "," otherwise TypeError
print(hair_single_tuple)

a, b = (1, 2)   # left of binary operator
del a, b        # right of unary statement

def f(x):
    return x, x ** 2
print(f(3))

for x, y in ((1, 1), (2, 4), (3, 9)):
    print(x, y)

eyes = ("brown", "hazel", "amber", "green", "blue", "gray")
colors = (hair, eyes)
print(colors)
print(colors[1][3:-1])

things = (1, -7.5, ("pea", (5, "xyz"), "queue"))
print(things[2][1][1][2])

MANUFACTURER, MODEL, SEATING = (0, 1, 2)
MINIMUM, MAXIMUM = (0, 1)
aircraft = ("Airbus", "A320-200", (100, 200))
print(aircraft[SEATING][MAXIMUM])

import math
for x, y in ((-3, 4), (5, 12), (28, -45)):
    print(math.hypot(x, y))
    
# Named tuples
import collections
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))
total = 0.0
for sale in sales:
    total += sale.quantity * sale.price
print("Total ${0:.2f}".format(total))

Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 200))
print(aircraft)
print(aircraft.seating.maximum)
print("{0} {1}".format(aircraft.manufacturer, aircraft.model))
print("{0.model} {0.seating.minimum}".format(aircraft))
print("{manufacturer} {model}".format(**aircraft._asdict()))