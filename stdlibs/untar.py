# -*- coding: utf-8 -*-
#
# File name     : untar.py
# Description   : Untar those tarballs files on Windows, Unix/Linux and Mac OS X platforms.
# Creator       : Frederick Hsu
# Creation date : Mon.  04 Nov. 2019
# Copyright(C)  2019    All rights reserved.
#

import tarfile
import string
import sys

BZ2_AVAILABLE = True
try:
    import bz2
except ImportError:
    BZ2_AVAILABLE = False

UNTRUSTED_PREFIXES = tuple(["/", "\\"] + [c + ":" for c in string.ascii_letters])

def error(message, exit_status = 1):
    print(message)
    sys.exit(exit_status)

def untar(archive):
    tar = None
    try:
        tar = tarfile.open(archive)
        for member in tar.getmembers():
            if member.name.startswith(UNTRUSTED_PREFIXES):
                print("untrusted prefix, ignoring", member.name)
            elif ".." in member.name:
                print("suspect path, ignoring", member.name)
            else:
                tar.extract(member)
                print("unpacked", member.name)
    except (tarfile.TarError, EnvironmentError) as err:
        error(err)
    finally:
        if tar is not None:
            tar.close()