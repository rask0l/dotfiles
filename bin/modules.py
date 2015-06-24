#!/usr/bin/python

import sys, yaml

def usage():
    print "You used it wrong."

if __name__ == "__main__":
    module_file = ""

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    module_file = sys.argv[1]

    with open(module_file, 'r') as stream:
        print(yaml.load(stream))


