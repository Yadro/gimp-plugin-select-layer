#!/usr/bin/env python

# import sys
# sys.stderr = open('c:\\temp\\gimpstderr.txt', 'w')
# sys.stdout = open('c:\\temp\\gimpstdout.txt', 'w')

from gimpfu import *
import select_layer_func

register(
    "select_layer_prev",
    "Select layer (prev)",
    "Select next layer",
    "Yadro",
    "Open source",
    "2017",
    "<Image>/Layers/Select layer (prev)",
    "*",
    [],
    [],
    select_layer_func.select_prev_layer)

main()
