# -*- coding: utf-8 -*-
#
# File name     : dicts.py
# Description   : Study the dictionary (or mapping) data type.
# Creator       : Frederick Hsu
# Creation date : Tue.      10 Sep. 2019
# Copyright(C)  2019    All rights reserved.
#

d1 = dict({"id":1948, "name":"Washer", "size":3})
print(d1)
d2 = dict(id = 1948, name = "Washer", size = 3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id":1948, "name":"Washer", "size":3}

dictionary = {"root":18, 
              "blue":[75, "R", 2], 
              21:"venus", 
              -14:None, 
              "mars":"rover",
              (4, 11):18,
              0:45}
print(dictionary["blue"])
dictionary["name"] = "Frederique Hsu"

print("\n")
for key, value in dictionary.items():
    print("key = {0}, value = {1}".format(key, value))
print("\n")

del dictionary[-14]
dictionary.pop(0)
print("There exists {0} key-value pairs now.".format(len(dictionary)))
print(dictionary.get("name"))
print(dictionary.values())
print(dictionary.popitem())

print("\n")
for value in dictionary.values():
    print(value)

print("\n")
for key in dictionary.keys():
    print(key)
    
#==============================================================================
print("\n")

d = {}.fromkeys("ABCD", 3)
s = set("ACX")
matches = d.keys() & s
print(matches)

greens = dict(green = "#0080000", olive = "#808000", lime = "#00FF00")
print("{green} {olive} {lime}".format(**greens))

#==============================================================================
print("\n")

import os
file_sizes = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}
for key, value in file_sizes.items():
    print("file_name = {0} \nfile_size = {1}\n".format(key, value))