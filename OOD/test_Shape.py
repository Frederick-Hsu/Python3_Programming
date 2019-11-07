# -*- coding: utf-8 -*-
#
# File name     : test_Shape.py
# Description   : Test and verify the Shape.py module
#

import Shape

p = Shape.Point(3, 9)
repr(p)

q = eval(p.__module__ + "." + repr(p))
print(repr(q))

print(str(q))

c = Shape.Circle(5, 28, 45)
print(p.distance_from_origin())
print(c.distance_from_origin())