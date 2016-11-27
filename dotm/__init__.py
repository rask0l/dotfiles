from . import cmd
import logging

log = None

def main(argv=None):
    configure_logger()
    log.debug("Executing __init__.py main()")
    log.debug("argv:" + str(argv))

    cmd.run(argv)

def configure_logger():
    global log
    log = logging.getLogger('dotm')
    log.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter.default_time_format = '%Y-%m-%d %H:%M:%S'
    formatter.default_msec_format = '%s.%03d'
    ch.setFormatter(formatter)

    log.addHandler(ch)


__all__ = ['main']
