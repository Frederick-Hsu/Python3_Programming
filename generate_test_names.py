# -*- coding: utf-8 -*-
#
# File name     : generate_test_names.py
# Description   : 
# Creator       : Frederick Hsu
# Creation date : Thu.  12 Sep. 2019
# Copyright(C)  2019    All rights reserved.
# 

def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"), 
                            (surnames, "data/surnames.txt")):
        for name in open(filename, encoding = "utf8"):
            names.append(name.strip())
    return forenames, surnames


# =============================================================================
# import os
# path.replace("/", os.sep)
# =============================================================================

import random

forenames, surnames = get_forenames_and_surnames()
fh = open("data/test-names.txt", "w", encoding = "utf8")
for index in range(100):
    line = "{0} {1}\n".format(random.choice(forenames), 
                              random.choice(surnames))
    fh.write(line)


limit = 100
years = list(range(1970, 2019)) * 3
fh = open("data/test-names2.txt", "w", encoding = "utf8")
for year, forename, surname in zip(random.sample(years, limit), 
                                   random.sample(forenames, limit), 
                                   random.sample(surnames, limit)):
    name = "{0} {1}".format(forename, surname)
fh.write("{0:.<25}.{1}\n".format(name, year))