#!/usr/bin/env python3

import logging
import os, sys
import dotm

log = logging.getLogger("dotm")

# To execute after cloning this repository,
# run from this file 'bin/dotm':
#   $ python3 dotm.py
# Or run from 'dotm/__main__.py':
#   $ python3 -m dotm
# Either executes main() in 'dotm/__init__.py'
#
# To build the pex with bazel, 
#   $ bazel build //:dotm
#


if __name__ == "__main__":
    log.debug("Executing bin/dotm")
    log.debug("argv:" + str(sys.argv))
    dotm.main(sys.argv)
