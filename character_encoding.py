# -*- coding: utf-8 -*-
#
# File name     : character_encoding.py
# Description   : Study the character encoding subject.
# Creator       : Frederick Hsu
# Creation date : Mon.  19 Aug. 2019
# Copyright(C)  2019    All rights reserved.
# 

artist = "Tage Asen"
print(artist.encode("Latin1"))
print(artist.encode("US_ASCII"))

name = "徐赞 (Frederique Hsu)"
# "Latin-1" cannot encode characters 徐赞, ordinal not in range (256)
# print(name.encode("Latin1"))  
print(name.encode("ascii", "replace"))
print(name.encode("ascii", "backslashreplace"))
print("{0!a}".format(name))
print(name.encode("UTF8"))
print(name.encode("UTF16"))
print((name.encode("UTF16")).decode("UTF16"))
print(name.encode("UTF8").decode("UTF8"))