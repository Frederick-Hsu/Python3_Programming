# -*- coding: utf-8 -*-
#
# File name     : apply_std_modules.py
# Description   : Apply some standard modules to study the actual cases.
#

import base64

binary = open("Beauty.jpeg", "rb").read()
ascii_text = ""
for i, c in enumerate(base64.b64encode(binary)):
    if i and i % 68 == 0:
        ascii_text += "\n"
    ascii_text += chr(c)

print(ascii_text)
# Save the binary data from a JPEG photo file to a text file.
open("my_lover.txt", "wb").write(base64.b64decode(ascii_text))