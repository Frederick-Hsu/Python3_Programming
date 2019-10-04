# -*- coding: utf-8 -*-
#
# File name     : composite_data.py
# Description   : Learn how to copy the objects of composite type.
# Creator       : Frederick Hsu
# Creation date : Fri.  04 Oct. 2019
# Copyright(C)  2019    All rights reserved.
#

songs = ["Because", "Boys", "Carol"]
beatles = songs
print(beatles, songs)

beatles[2] = "Cayenne"
print(beatles, songs)

beatles = songs[:]      # Get the entire copy
beatles[1] = "Paradise"
print(beatles, songs)

domain_names_dict = {"cn":"China", "us":"America", "de":"Germany"}
copy_of_domain_names = domain_names_dict.copy()

copy_of_domain_names["uk"] = "British"
print(domain_names_dict, "\n", copy_of_domain_names)

domains = dict(copy_of_domain_names)
domains["us"] = "United States of America"
print("{0}\n{1}".format(copy_of_domain_names, domains))

print("\n==================================================================\n")

x = [53, 68, ["A", "B", "C"]]
y = x[:]    # Shadow copy
print("{0}\n{1}".format(x, y))
y[1] = 40
x[2][1] = "Q"
print("{0}\n{1}".format(x, y))

import copy
z = copy.deepcopy(x)    # Deep copy
x[2][2] = "M"
z[2][0] = "Plan"
print("{0}\n{1}".format(x, z))