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

import math
import sys
print("math.pi == {0.pi} sys.maxunicode == {1.maxunicode}".format(math, sys))

# You can omit the field name in Python 3.1
print("{} {} {}".format("Python", "can", "count"))

# Split the mapping, and access the key and values throught the locals() function
element = "Silver"
number = 47
print("Element {number} is {element}".format(**locals()))   # ** is the dictionary splitting operator

print("The {animal} weights {weight}kg".format(**animal_weight))    # ** can split the dictionary

print("\n==================================================================\n")

# Converting the fields
import decimal
decimal_number = decimal.Decimal("3.0259846")
print(decimal_number)
print("{0}, {0!s}, {0!r}, {0!a}".format(decimal_number))

sword = "The sword of truth"
print("'{0:30}'".format(sword))   # minimum width 30
print("'{0:>30}'".format(sword))    # right align, minimum width 30
print("'{0:^30}'".format(sword))    # center align, minimum width 30
print("'{0:-^30}'".format(sword))   # - fill, center align, minimum width 30
print("'{0:.<30}'".format(sword))   # . fill, left align, minimum width 30
print("'{0:.10}'".format(sword))    # maximum width 10

maxwidth = 12
print("'{0}'".format(sword[:maxwidth]))
print("'{0:.{1}}'".format(sword, maxwidth))

number = 5938
print("'{0:0=20}'".format(number))      # 0 fill, minimum width 20
print("'{0:0=20}'".format(-number))     # 0 fill, minimum width 20
print("'{0:020}'".format(number))       # 0-pad and minimum width 20
print("'{0:020}'".format(-number))      # 0-pad and minimum width 20

align_number = 18340427
print("'{0:*<18}'".format(align_number))    # * fill, left align, min width 18
print("'{0:*>18}'".format(align_number))    # * fill, right align, min width 18
print("'{0:*^18}'".format(align_number))    # * fill, center align, min width 18
print("'{0:*^18}'".format(-align_number))   # * fill, center align, min width 18

print("[{0: }]\n[{1: }]\n".format(align_number, -align_number))    # space or - sign
print("[{0:+}]\n[{1:+}]\n".format(align_number, -align_number))     # force sign
print("[{0:-}]\n[{1:-}]\n".format(align_number, -align_number))     # - sign if needed

print("{0:b}\t{0:o}\t{0:x}\t\t{0:X}".format(align_number))
print("{0:#b}\t{0:#o}\t{0:#x}\t{0:#X}".format(align_number))

print("{0:,} {0:*>18,}".format(2.39432185e6))

import locale
locale.setlocale(locale.LC_ALL, "")

real, imag = (1234567890, 12345.68)
print("{0:n} \t {1:n}".format(real, imag))

locale.setlocale(locale.LC_ALL, "C")
print("{0:n} \t {1:n}".format(real, imag))

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
print("{0:n} \t {1:n}".format(real, imag))

locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
print("{0:n} \t {1:n}".format(real, imag))