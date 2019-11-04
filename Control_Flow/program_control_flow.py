# -*- coding: utf-8 -*-
#
# File name     : program_control_flow.py
#

import sys

offset = 20
if not sys.platform.startswith("win"):
    offset = 0
    

offset = 20 if not sys.platform.startswith("win") else 10
print(offset)

margin = False
width = 100 + (10 if margin else 0)
print(width)


count = 2
print("{0} file{1}".format((count if count != 0 else "no"), ("s" if count > 1 else "")))

# =============================================================================
# def list_find(lst, target):
#     index = 0
#     while index < len(lst):
#         if lst[index] == target:
#             break
#         index += 1
#     else:
#         index = -1
#     return index
# 
# def list_find(lst, target):
#     for index, x in enumerate(lst):
#         if x == target:
#             break
#     else:
#         index = -1
#     return index
# =============================================================================

def list_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index

print("\n==================================================================\n")

def find_table(table, target):
    found = False
    for row, record in enumerate(table):
        for column, field in enumerate(record):
            for index, item in enumerate(field):
                if item == target:
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        print("found at ({0}, {1}, {2})".format(row, column, index))
    else:
        print("not found")


class FoundException(Exception):
    pass

def table_find(table, target):
    try:
        for row, record in enumerate(table):
            for column, field in enumerate(record):
                for index, item in enumerate(field):
                    if item == target:
                        raise FoundException()
    except FoundException:
        print("found at ({0}, {1}, {2})".format(row, column, index))
    else:
        print("not found")