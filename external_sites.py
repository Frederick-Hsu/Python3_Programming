# -*- coding: utf-8 -*-
#
# File name     : external_sites.py
# Description   : Read a HTML file, and list the websites which are unique.
# Creator       : Frederick Hsu
# Creation date : Wed.  11 Sep. 2019
# Copyright(C)  2019    All rights reserved.
#

import sys

sites = {}
for filename in sys.argv[1:]:
    for line in open(filename):
        i = 0
        while True:
            site = None
            i = line.find("https://", i)
            if i > -1:
                i += len("https://")
                for j in range(i, len(line)):
                    if not (line[j].isalnum() or line[j] in ".="):
                        site = line[i:j].lower()
                        break
                if site and "." in site:
                    sites.setdefault(site, set()).add(filename)
# =============================================================================
#                     if site not in sites:
#                         sites[site] = set()
#                     sites[site].add(filename)
# =============================================================================
                    i = j
                else:
                    break
for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key = str.lower):
        print("    {0}".format(filename))