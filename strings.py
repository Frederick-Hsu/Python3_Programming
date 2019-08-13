# -*- coding: utf-8 -*-
#
# File name     : strings.py
# Description   : Delve the topic of string in the Python lang. 
# Creator       : Frederick Hsu
# Creation date : Fri.  09 Aug. 2019
# Copyright(C)  2019    All rights reserved.
#

empty_str = str()
print("The empty string is : ", empty_str)

text = '''A triple quoted string like this can include 'quotes' and
"quotes" without formality. We can also escape newlines \
so this particular string is actually only two lines long.'''
print(text)

str_a = "Single 'quotes' are fine; \"double\" must be escaped."
escaped_str_b = 'Single \'quotes\' must be escaped; "doubles" are file.'
# =============================================================================
# print(str_a)
# print(escaped_str_b)
# =============================================================================

import re
phone = re.compile("^((?:[(]\\d+[)])?\\s*\\d+(?:-\\d+)?)$")  # regular expression

t = "This is not the best way to join two long strings " + \
    "together since it relies on ugly newline escaping";
    
# Python文档建议总是使用圆括号将跨越多行的任何语句进行封装，而不使用转义的换行符。
s = ("This is the nice way to join two long strings "
     "together; it relies on string literal concatenation.")
print(t)
print(s)

euros = "\N{euro sign} \u20AC \U000020AC"
print(euros)
print(ord(euros[0]))
print(hex(ord(euros[0])))

unicode_str = "anarchists are " + chr(8734) + chr(0x23B7)
print(unicode_str)
print(ascii(unicode_str))

unichar = chr(0x00C5)
print(unichar)

import unicodedata
# NFKD : Normalization Form Compatibility Decomposition
print(unicodedata.normalize("NFKD", unichar))   

print("\n==================================================================\n")

# String slicing and steps
test_str = "Madame Tussauds waxwork museum"
print(test_str)
print(test_str[4:12])
print(test_str[2:15:3])
print(test_str[::-1])

print("str.capitalize() = ", test_str.capitalize())
print("str.upper() = ", test_str.upper())

print(test_str.count("m", 6) == test_str[6:].count("m"))
print(test_str.count("m", 5, -3) == test_str[5:-3].count("m"))

treatises = ["Arithmetica", "Conics", "Elements"]
print(" ".join(treatises))
print("-<>-".join(treatises))

# repeat string
repeat = "="*5
print(repeat)
repeat *= 10
print(repeat)

def extract_from_tag_M(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None

def extract_from_tag_N(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer, start)
        if j != -1:
            return line[start:j]
    return None

print(extract_from_tag_M("red", "what a <red>rose</red> this is"))
print(extract_from_tag_N("red", "what a <red>rose</red> this is"))

digits = "\N{circled digit five}053"
print("The ", digits, " is digit or not : ",  digits.isdigit())

# Split the string by delimiter user specified.
record = "Leo Tolstoy*1828-8-28*1910-11-20"
segments = record.split("*")
print(segments)
born = segments[1].split("-")
died = segments[2].split("-")
print(segments[0] + " had lived about", (int(died[0]) - int(born[0])), "years.")

table = "".maketrans("\N{bengali digit zero}"
                     "\N{bengali digit one}"
                     "\N{bengali digit two}"
                     "\N{bengali digit three}"
                     "\N{bengali digit four}"
                     "\N{bengali digit five}"
                     "\N{bengali digit six}"
                     "\N{bengali digit seven}"
                     "\N{bengali digit eight}"
                     "\N{bengali digit nine}",
                     "0123456789")
print(table)
print("20749".translate(table))
print("\N{bengali digit two}07\N{bengali digit four}\N{bengali digit nine}".translate(table))