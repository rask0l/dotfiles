import sys
import dotm
import logging

log = logging.getLogger("dotm")

if __name__ == '__main__': 
    log.debug("Executing __main__.py")
    log.debug("argv:" + str(sys.argv))
    dotm.main(sys.argv)

