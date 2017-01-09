#!/usr/bin/env python

# import sys
# sys.stderr = open('c:\\temp\\gimpstderr.txt', 'w')
# sys.stdout = open('c:\\temp\\gimpstdout.txt', 'w')

from gimpfu import *
import select_layer_func

register(
    "select_layer_next",
    "Select layer (next)",
    "Select next layer",
    "Yadro",
    "Open source",
    "2017",
    "<Image>/Layers/Select layer (next)",
    "*",
    [],
    [],
    select_layer_func.select_next_layer)

main()
