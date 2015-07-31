#!/usr/bin/python

modules = ["yaml"]

def check_deps_installed():
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print "You are missing a dependency: " + module
            return False
    return True

if __name__ == "__main__":
    check_deps_installed()
