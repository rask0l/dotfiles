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

def print_list(l):
    s = ""
    for idx,item in enumerate(l):
        if idx != len(l)-1:
            s += str(item) + ", "
        else:
            s += str(item) + "\n"
    print(s)


def path_exists(path):
    return os.path.lexists(path)
