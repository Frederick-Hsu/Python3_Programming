#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File name     : csv2html2_opt.py
# Description   : Convert the CSV to HTML format, and it support the command line arguments.
# Creator       : Frederique Hsu
# Creation date : Fri.  01 Nov. 2019
# Copyright(C)  2019    All rights reserved.
#

import optparse

def man():
    parser = optparse.OptionParser()
    parser.add_option("-w", "--maxwidth", dest = "maxwidth", type = "int", 
                      help = ("the maximum number of character that can be "
                              "output to string fields [default: %default]"))
    parser.add_option("-f", "--format", dest = "format",
                      help = ("the format used for outputting numbers "
                              "[default: %default]"))
    parser.set_defaults(maxwidth = 100, format = ".0f")
    opts, args = parser.parse_args()impo 