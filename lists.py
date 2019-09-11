# -*- coding: utf-8 -*-
#
# File name     : lists.py
# Description   : Study the subject of list
# Creator       : Frederique Hsu
# Creation date : Wed.  21 Aug. 2019
# Copyright(C)  2019    All rights reserved.
#

lst = [-17.6, "kilo", 49, 'V', ["ram", 5, "echo"], 7]
print("This list has {0} elements in length.".format(len(lst)))

first, *rest = [9, 2, -4, 8, 7]
print("first variable = {0}, rest variable = {1}".format(first, rest))

# 序列拆分操作符 *mid
begin, *mid, end = "Charles Philips Arthur George Windsor".split()
print(begin, mid, end)

*directories, executable = "/usr/local/bin/gvim".split("/")
print(directories, executable)

def product(a, b, c):
    return a * b * c    # here * is the multiplication operator

print("product(2, 3, 5) = {0}".format(product(2, 3, 5)))
L = [2, 3, 5]
print("L = ", L)
print("product(*L) = {0}".format(product(*L)))
print("product(2, *L[1:]) = {0}".format(product(2, *L[1:])))

# 使用del语句删除项
x = 8146    # object ref. 'x' is created; int of value 8146 created
print("x = ", x)
del x   # object ref. 'x' deleted; int ready for garbage collection
# x     # NameError pops up, because name 'x' is not defined, since you del x in previous line

for index in range(len(L)):
    L[index] += 1
print("L = ", L)

woods = ["Cedar", "Yew", "Fir"]
woods += ["Kauri", "Larch"]     # extend the list
print("woods = {0}".format(woods))

woods.insert(2, "Pine")
print("woods =", woods)

woods.append("Spruce")
print("woods = {0}".format(woods))

woods[3:3] = ["Sequoia"]
print("woods =", woods)

woods[1:3] = ["Sugi", "Rimu", "Chinar"]
print("woods = {0}".format(woods))

woods.pop()
print("woods = {0}".format(woods))

woods.pop(4)
print("woods = {0}".format(woods))

woods.remove("Sugi")
print("woods = {0}".format(woods))

del woods[4]
print("woods = {0}".format(woods))

woods[1:3] = []
print("woods = {0}".format(woods))

print("\n==================================================================\n")

alphabet = ["A", "B", "C", "D", "E", "F"]
print("alphabet = {0}".format(alphabet))
alphabet[2:5] = ["X", "Y"]
print("alphabet = {0}".format(alphabet))

print("\n==================================================================\n")

natrual_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_number = natrual_number[::2]
print("odd numbers are {0}".format(odd_number))
even_number = natrual_number[1::2]
print("even numbers are {0}".format(even_number))
natrual_number[1::2] = [0] * len(natrual_number[1::2])
print("After replaced even numbers, the natural number list become to {0}".format(natrual_number))

print("\n==================================================================\n")

leaps = []
for year in range(1900, 2021):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leaps.append(year)
print("Leap years list : {0}".format(leaps))

leap_years = [year for year in range(1980, 2021)
                  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
print(leap_years)

codes = []
for sex in "MF":    # Male, Female
    for size in "SMLX":     # Small, Medium, Large, eXtra large
        if sex == "F" and size == "X":
            continue
        for color in "BGW":     # Black, Gray, White
            codes.append(sex + size + color)
print(codes)

codes_alias = [sex + size + color for sex in "MF" for size in "SMLX" for color in "BGW" if not (sex == "F" and size == "X")]
print(codes_alias)