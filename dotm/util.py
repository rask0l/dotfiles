import os

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def list_dirs(dirname, ignore):
    """ List dirs in dirname that are not in ignore """
    dirs = []
    entries = os.listdir(dirname)
    for e in entries:
        d = os.path.join(dirname, e)
        if os.path.isdir(d) and e not in ignore:
            dirs.append(e)
    return dirs

def abs(*args):
    return os.path.abspath(os.path.join(*args))

def usr(*args):
    return os.path.expanduser(os.path.join(*args))

