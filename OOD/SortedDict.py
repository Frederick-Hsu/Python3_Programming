# -*- coding: utf-8 -*-
#
# File name     : SortedDict.py
#

'''
SortedDict - provide a dict collection, whose keys are sorted. 

>>> d = SortedDict(dict(s = 1, A = 2, y = 6), str.lower)
>>> d["z"] = 4
>>> # print(str(d))
>>> d["T"] = 5
>>> del d["y"]
>>> d["n"] = 3
>>> d["A"] = 17
>>> str(d)
"{'A': 17, 'n': 3, 's': 1, 'T': 5, 'z': 4}"

'''

import SortedList

class SortedDict(dict):
    def __init__(self, dictionary = None, key = None, **kwargs):
        dictionary = dictionary or {}
        super().__init__(dictionary)
        if kwargs:
            super().update(kwargs)
        self.__keys = SortedList.SortedList(super().keys(), key)
    
    def update(self, dictionary = None, **kwargs):
        if dictionary is None:
            pass
        elif isinstance(dictionary, dict):
            super().update(dictionary)
        else:
            for key, value in dictionary.items():
                super().__setitem__(key, value)
        if kwargs:
            super().update(kwargs)
        self.__keys = SortedList.SortedList(super().keys, self.__keys.key)
        
    @classmethod
    def fromkeys(cls, iterable, value = None, key = None):
        return cls({k : value for k in iterable}, key)
    
    def __setitem__(self, key, value):
        if key not in self:
            self.__keys.add(key)
        return super().__setitem__(key, value)
    
    def __delitem__(self, key):
        try:
            self.__keys.remove(key)
        except ValueError:
            raise KeyError(key)
        return super().__delitem__(key)
    
    def setdefault(self, key, value = None):
        if key not in self:
            self.__keys.add(key)
        return super().setdefault(key, value)
    
    def pop(self, key, *args):
        if key not in self:
            if len(args) == 0:
                raise KeyError(key)
            return args[0]
        self.__keys.remove(key)
        return super().pop(key, args)
    
    def popitem(self):
        item = super().popitem()
        self.__keys.remove(item[0])
        return item
    
    def clear(self):
        super().clear()
        self.__keys.clear()
    
    def values(self):
        for key in self.__keys:
            yield self[key]
    
    def items(self):
        for key in self.__keys:
            yield (key, self[key])
    
    def __iter__(self):
        return iter(self.__keys)
    
    keys = __iter__     # create the keys object reference, same as def keys(self):
    
    def __repr__(self):
        return object.__repr__(self)
    
    def __str__(self):
        items = []
        for key, value in self.items():
            items.append("{0!r}: {1!r}".format(key, value))
        return "{" + ", ".join(items) + "}"
    
    def copy(self):
        d = SortedDict()
        super(SortedDict, d).update(self)
        d.__keys = self.__keys.copy()
        return d

    __copy__ = copy
    
    def value_at(self, index):
        return self[self.__keys[index]]
    
    def set_value_at(self, index, value):
        self[self.__keys[index]] = value

# =============================================================================
# # Build and return a list
# def letter_range(a, z):
#     result = []
#     while ord(a) < ord(z):
#         result.append(a)
#         a = chr(ord(a) + 1)
#     return result
# =============================================================================

# Return each value on demand
def letter_range(a, z):
    while ord(a) < ord(z):
        yield a
        a = chr(ord(a) + 1)
#==============================================================================

if __name__ == "__main__":
    
    class MyDict(SortedDict):
        pass
    
    d = MyDict.fromkeys("VEINS", 3)
    print(str(d))
    print(d.__class__.__name__)
    
    import doctest
    doctest.testmod()