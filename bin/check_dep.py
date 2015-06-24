#!/usr/bin/python

import sys

modules = ["yaml"]

for module in modules:
    try:
        __import__(module)
    except ImportError:
        print "You are missing a dependency: " + module
        sys.exit(1)

