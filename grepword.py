# -*- coding: utf-8 -*-
#
# File name     : grepword.py
# Description   : Simulate the Linux command "grep" function
# Creator       : Frederique Hsu
# Creation date : Thu.  12 Sep. 2019
# Copyright(C)  2019    All rights reserved.
#

import sys

if len(sys.argv) < 3:
    print("usage: grepword.py word infile1 [infile2 [... infileN]]")
    print("for example : grepword.py Dom data/forenames.txt")
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]:
    for line_no, line in enumerate(open(filename), start = 1):
        if word in line:
            print("{0}:{1}:{2:.40}".format(filename, line_no, line.strip()))