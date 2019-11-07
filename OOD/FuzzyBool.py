# -*- coding: utf-8 -*-
#
# File name     : FuzzyBool.py
# Description   : Define and implement a complete class FuzzyBool
# Creator       : Frederick Hsu
# Creation date : Tue.  05 Nov. 2019
# Copyright(C)  2019    All rights reserved.
#

class FuzzyBool:
    def __init__(self, value = 0.0):
        self.__value = value if 0.0 <= value <= 1.0 else 0.0
    
    def __invert__(self):
        return FuzzyBool(1.0 - self.__value)
    
    def __and__(self, other):
        return FuzzyBool(min(self.__value, other.__value))
    
    def __iand__(self, other):
        self.__value = min(self.__value, other.__value)
        return self
    
    def __or__(self, other):
        return FuzzyBool(max(self.__value, other.__value))
    
    def __ior__(self, other):
        self.__value = max(self.__value, other.__value)
        return self
    
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, self.__value))
    
    def __str__(self):
        return str(self.__value)
    
    def __bool__(self):
        return self.__value > 0.5
    
    def __int__(self):
        return round(self.__value)
    
    def __float__(self):
        return self.__value
    
    def __lt__(self, other):
        return self.__value < other.__value
    
    def __eq__(self, other):
        return self.__value == other.__value
    
    def __le__(self, other):
        return self.__value <= other.__value
    
    def __hash__(self):
        return hash(id(self))
    
    def __format__(self, format_spec):
        return format(self.__value, format_spec)
    
    @staticmethod
    def conjuction(*fuzzies):
        return FuzzyBool(min([float(x) for x in fuzzies]))
    
    @staticmethod
    def disjunction(*fuzzies):
        return FuzzyBool(max([float(x) for x in fuzzies]))
    
    def __abs__(self):
        return abs(self.__value)
    
    def __index__(self):
        return bin(self.__value), oct(self.__value), hex(self.__value)
    
    def __pos__(self):
        return +self.__value
    
    def __add__(self, other):
        return self.__value + other.__value
    
    def __iadd__(self, other):
        self.__value = self.__value + other.__value
        return self
    
    def __rand__(self, other):
        return other.__value + self.__value
    
    def __mul__(self, other):
        return self.__value * other.__value
    
    def __imul__(self, other):
        self.__value = self.__value * other.__value
        return self
    
    def __rmul__(self, other):
        return other.__value * self.__value
    
    def __floordiv__(self, other):
        return self.__value // other.__value
    
    def __ifloordiv__(self, other):
        self.__value = self.__value // other.__value
        return self
    
    def __rfloordiv__(self, other):
        return other.__value // self.__value
    
    def __divmod__(self, other):
        return divmod(self.__value, other.__value)
    
    def __pow__(self, other):
        return self.__value ** other.__value
    
    def __ipow__(self, other):
        self.__value = self.__value ** other.__value
        return self
    
    def __rpow(self, other):
        return other.__value ** self.__value