#!/usr/bin/env python
import sys
file = 'xiaotuan.png'

try:
    png = open(file)
except IOError:
    sys.exit("could not open file")
    
