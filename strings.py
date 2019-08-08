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