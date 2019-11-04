# -*- coding: utf-8 -*-
#
# File name     : file_directory_process.py
# Description   : Study the standard libraries, which are used to handle with file, directory and process.
# Creator       : Frederick Hsu
# Creation date : Mon.  04 Nov. 2019
# Copyright(C)  2019    All rights reserved.
#

import shutil
dir(shutil)
help(shutil)
help(shutil.copy)
help(shutil.copytree)
help(shutil.move)
help(shutil.rmtree)

import tempfile
help(tempfile)
help(tempfile.mkstemp)

import filecmp
help(filecmp.cmp)
help(filecmp.cmpfiles)

import subprocess
help(subprocess)

import multiprocessing
help(multiprocessing)

import os
help(os)
print(os.getcwd())