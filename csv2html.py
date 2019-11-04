# -*- coding: utf-8 -*-
#
# File name     : csv2html.py
# Description   : Read data from a .csv file, and convert to the HTML format.
# Creator       : Frederick Hsu
# Creation date : Tue.  20 Aug. 2019
# Copyright(C)  2019    All rights reserved.
#

import sys

def print_start():
    print("<table border = '1'>")

def print_end():
    print("</table>")

def print_line(line, color, maxwidth):
    print("<tr bgcolor = '{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
    else:
        number = field.replace(",", "")
        try:
            x = float(number)
            print("<td align = 'right'>{0:d}</td>".format(round(x)))
        except ValueError:
            field = field.title()
            field = field.replace("And", "and")
            if len(field) <= maxwidth:
                field = escape_html(field)
            else:
                field = "{0}...".format(escape_html(field[:maxwidth]))
            print("<td>{0}</td>".format(field))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"":
            if quote is None:   # start of quoted string
                quote = c
            elif quote == c:    # end of quoted string
                quote = None
            else:
                field += c      # other quote inside quoted string
            continue
        if quote is None and c == ",":      # end of a field
            fields.append(field)
            field = ""
        else:
            field += c      # accumulating a field
    if field:
        fields.append(field)    # adding the last field
    return fields

def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()

if __name__ == "__main__":
    main()