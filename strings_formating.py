# -*- coding: utf-8 -*-
#
# File name     : strings_formating.py
# Description   : Study the topic of formatting the strings
# Creator       : Frederick Hsu
# Creation date : Wed.  14 Aug. 2019
# Copyright(C)  2019    All rights reserved.
#

formatted_string = "The novel '{0}' was published in {1}".format("Hard Times", 1854)
print(formatted_string)

print("{{{0}}} {1}; -}}".format("I'm in braces", "I'm not"))
print("{0}{1}".format("The amount due is $", 200))

x = "three"
s = "{0} {1} {2}"
s = s.format("The", x, "tops")
print(s)

# Substitute the field name
print("{who} turned {age} this year".format(age = 88, who = "She"))
# positional arguments must follow keyword argument
print("The {who} was {0} last week".format(12, who = "boy"))    

stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
print("We have {0[1]} and {0[2]} in stock".format(stock))

animal_weight = dict(animal = "elephant", weight = 12000)
print("The {0[animal]} weights {0[weight]}kg.".format(animal_weight))