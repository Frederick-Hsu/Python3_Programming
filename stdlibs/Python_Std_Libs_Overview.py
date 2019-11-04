#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File name     : Python_Std_Libs_Overview.py
# Description   : List some standard libraries of Python, have an overview on them.
# Creator       : Frederick Hsu
# Creation date : Fri.  01 Noc. 2019
# Copyright(C)  2019    All rights reserved.
#


# String Processing
import string
dir(string)
help(string)

import struct
dir(struct)
help(struct)

import textwrap
dir(textwrap)
help(textwrap)

import difflib
dir(difflib)
help(difflib)

import re
dir(re)
help(re)

#==============================================================================
print("\n==================================================================\n")

print("io.StringIO class")

import io
dir(io)
help(io)

from io import StringIO
dir(StringIO)
help(StringIO)

import sys
print("An error message", file = sys.stdout)
sys.stdout.write("Another error message\n")

print("This is a new line. ", end = "")
print("But we can set the end keyword argument to eliminate the Line-Feed.")

# sys.stdout = StringIO()

print("Now the StringIO object will capture all text which are originally output to \
      the sys.stdout console.")
sys.stdout.write("But we can disable this behaviour, restore the original sys.stdout output, \
                 by using the statement: sys.stdout = sys.__stdout__")

# sys.stdout = sys.__stdout__
print("Here it has already restored.")

# io.StringIO.getvalue()

#==============================================================================
print("\n==================================================================\n")

print("Command Line programs")

import fileinput
dir(fileinput)
help(fileinput)

import optparse
dir(optparse)

import getopt
dir(getopt)

#==============================================================================
print("\n==================================================================\n")

# Math and Number
import decimal
dir(decimal)
help(decimal)

import fractions
dir(fractions)
help(fractions)

import math
dir(math)
import cmath
dir(cmath)
import random
dir(random)
help(random)

import numbers
x = 5 + 8j
print(isinstance(x, numbers.Complex))
print(isinstance(10.25, numbers.Real))
print(isinstance(36, numbers.Integral))

import numpy
dir(numpy)
help(numpy)

import scipy
dir(scipy)
help(scipy)

#==============================================================================
print("\n==================================================================\n")

# Time and calendar
from calendar import *
dir(calendar)
help(calendar)

from datetime import *
dir(datetime)
help(datetime)

import dateutil
dir(dateutil)
help(dateutil)

import time
dir(time)
help(time)

moon_datetime_a = datetime(1998, 7, 20, 20, 17, 40)
moon_time = timegm(moon_datetime_a.utctimetuple())
print(moon_time)

moon_datetime_b = datetime.utcfromtimestamp(moon_time)
print(moon_datetime_b)
print(moon_datetime_a.isoformat())
print(moon_datetime_b.isoformat())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(moon_time)))

current_date_time = datetime.utcnow()
print(current_date_time)    # Current timestamp
print(time.time())      # The total seconds of current date and time
print(time.mktime(time.localtime()))


#==============================================================================
print("\n==================================================================\n")

# Algorithm and combination data type
import bisect
dir(bisect)
help(bisect)

import heapq
dir(heapq)
help(heapq)

import collections
help(collections.defaultdict)
help(collections.namedtuple)
help(collections.UserList)
help(collections.UserDict)
help(collections.UserString)
help(collections.deque)
help(collections.OrderedDict)
help(collections.Counter)

import array
help(array.array)

import weakref
dir(weakref)
help(weakref)

#==============================================================================
print("\n==================================================================\n")

# heapq module
import heapq
heap = []
heapq.heappush(heap, (5, "rest"))
heapq.heappush(heap, (2, "work"))
heapq.heappush(heap, (4, "study"))

for x in heapq.merge([1, 3, 4, 8], [2, 4, 7], [0, 1, 6, 8, 9]):
    print(x, end = " ")


#==============================================================================
print("\n==================================================================\n")

# File format, encoding and data persistence

import base64
print(dir(base64))

import quopri
for item in dir(quopri):
    print(item)

import uu
print(dir(uu), "\n")

import xdrlib
print(dir(xdrlib), "\n")

import bz2
help(bz2)

import gzip
print(dir(gzip), "\n")

import tarfile
print(dir(tarfile), "\n")

import zipfile
help(zipfile)

import gzip
help(gzip)

import aifc
help(aifc)

import wave
help(wave)

import audioop
help(audioop)

import sndhdr
help(sndhdr)

import configparser
help(configparser)

import csv
help(csv)

import pickle
help(pickle)

import shelve
help(shelve)