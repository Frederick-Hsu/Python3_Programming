# -*- coding: utf-8 -*-
#
# File name     : sets.py
# Description   : Study the set data type
# Creator       : Frederick Hsu
# Creation date : Tue.  10 Sep. 2019
# Copyright(C)  2019    All rights reserved.
#

collection = {7, "veil", 0, -29, ("x", 11), "Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat", frozenset({8, 4, 7}), 913}
print("the length of collection is: {0}".format(len(collection)))

empty_set = set()
empty_set.add("Frederique")
empty_set.add("Sun")
empty_set.add("Sat")

collection.add("Hsu")
empty_set.add("Hsu")
print(collection)

diff_set = collection.difference(empty_set)
print(collection)
print(diff_set)

intersect = collection.intersection(empty_set)
print(intersect)

print(collection.isdisjoint(empty_set))
print(collection.issubset(empty_set))
print(collection.issuperset(empty_set))

print(collection.pop())
print(collection.remove("Sun"))
print(collection.symmetric_difference(empty_set))
print(collection.symmetric_difference_update(empty_set))
print(collection.union(empty_set))
print(collection.update(empty_set))

pecan = set("pecan")
pie = set("pie")
print(pecan | pie, pecan.union(pie))
print(pecan & pie, pecan.intersection(pie))
print(pecan - pie, pecan.difference(pie))
print(pecan ^ pie, pecan.symmetric_difference(pie))
print(sorted(pecan))


import sys
if (len(sys.argv) == 1) or (sys.argv[1] in {"-h", "--help"}):
    print("No argument")
    
# =============================================================================
# filenames = set(filenames)
# for makefile in {"Makefile", "MAKEFILE", "makefile"}:
#     filenames.discard(makefile)
# =============================================================================
files = {"basics.htm", "help.html", "lists.py", "co2-sample.html", ".gitignore"}
html = {file for file in files
            if file.lower().endswith((".htm", "html"))}
print(html)

fixset = frozenset({"love", "is", "forever"})
print(fixset)