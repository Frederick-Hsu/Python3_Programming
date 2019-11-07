# -*- coding: utf-8 -*-
#
# File name     : ShapeAlt.py
# Description   : Alternate to the module Shape
#

import math

import Shape

class CircleAlt(Shape.Point):
    def __init__(self, radius, x = 0, y = 0):
        super().__init__(x, y)
        self.radius = radius
    
    @property
    def area(self):
        '''
        Calculate the area of a circle, with its radius
        
        >>> circle = CircleAlt(5, 3, 4)
        >>> circle.area
        78.53981633974483
        '''
        return math.pi * (self.radius ** 2)
    
    @property
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin - self.radius)
    
    @property
    def radius(self):
        '''
        The circle's radius
        
        >>> circle = CircleAlt(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        
        >>> circle = CircleAlt(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        
        >>> circle.radius = 6
        '''
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        assert radius > 0, "radius must be nonzero and non-negative"
        self.__radius = radius
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()