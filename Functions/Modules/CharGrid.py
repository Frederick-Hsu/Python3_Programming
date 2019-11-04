#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File name     : CharGrid.py
# Description   : Plot the grid just in the characters.
# Creator       : Frederick Hsu
# Creation date : Fri.  01 Nov. 2019
# Copyright(C)  2019    All rights reserved.
#

'''
Plot the grid just in some characters.

CharGrid module will store some characters in the memory, this module will provide
some functions, used to plot the line, rectangle and text in the grid of screen,
and display them in the console screen.

>>> resize(14, 50)
>>> add_rectangle(0, 0, *get_size())
>>> add_vertical_line(5, 10, 13)
>>> add_vertical_line(2, 9, 12, "!")
>>> add_horizontal_line(3, 10, 20, "+")
>>> add_rectangle(0, 0, 5, 5, "%")
>>> add_rectangle(5, 7, 12, 40, "#", True)
>>> add_rectangle(7, 9, 10, 38, " ")
>>> add_text(8, 10, "This is the CharGrid module")
>>> add_text(1, 32, "Pleasantville", "@")
>>> add_rectangle(6, 42, 11, 46, fill = True)
>>> render(False)
'''

import sys
import subprocess

class RangeError(Exception):
    pass

class RowRangeError(RangeError):
    pass

class ColumnRangeError(RangeError):
    pass

_CHAR_ASSERT_TEMPLATE = ("char must be a single character: '{0}'"
                         "is too long")
_max_rows = 25
_max_columns = 80
_grid = []
_background_char = " "

if sys.platform.startswith("win"):
    def clear_screen():
        subprocess.call(["cmd.exe", "/C", "cls"])
else:
    def clear_screen():
        subprocess.call(["clear"])

# =============================================================================
# def clear_screen():
#     command = (["clear"] if not sys.platform.startswith("win") else ["cmd.exe", "/C", "cls"])
#     subprocess.call(command)
# =============================================================================

clear_screen.__doc__ = '''Clears the screen using the underlying \
window system's clear screen command
'''

def resize(max_rows, max_columns, char = None):
    '''
    Changes the size of grid, wiping out the contents and changing the background
    if the background char is not None.
    '''
    assert max_rows > 0 and max_columns > 0, "too small"
    global _grid, _max_rows, _max_columns, _background_char
    if char is not None:
        assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
        _background_char = char
        _max_rows = max_rows
        _max_columns = max_columns
        _grid = [[_background_char for column in range(_max_columns)] for row in range(_max_rows)]
# =============================================================================
#         _grid = []
#         for row in range(_max_rows):
#             _grid.append([])
#             for column in range(_max_columns):
#                 _grid[-1].append(_background_char)
# =============================================================================

def add_horizontal_line(row, column0, column1, char = "-"):
    '''
    Adds a horizontal line to the grid using the given char.
    
    >>> add_horizontal_line(8, 20, 25, "=")
    >>> char_at(8, 20) == char_at(8, 24) == "="
    True
    >>> add_horizontal_line(31, 11, 12)
    Traceback (most recent call last):
    ...
    RowRangeError
    '''
    assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
    try:
        for column in range(column0, column1):
            _grid[row][column] = char
    except IndexError:
        if not 0 <= row <= _max_rows:
            raise RowRangeError()
        raise ColumnRangeError()

resize(_max_rows, _max_columns)

if __name__ == "__main__":
    import doctest
    doctest.testmod()