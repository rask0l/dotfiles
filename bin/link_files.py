#!/usr/bin/python

import yaml
import os
import sys


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def link_module(module_name):

    with open("../dotfiles/" + module_name + "/module.yaml", 'r') as stream:
        module = yaml.load(stream)
  
    if not module:
        return

    for file in module['files']:
        name = ""
        
        if file.keys()[0]:
            name = file.keys()[0]
        else:
            print("You must give each file a name.")
            continue
    
        src_file_name, dest_file_name = file.iteritems().next() 
        src = os.path.abspath(find( src_file_name, "../dotfiles/"))
        dest = os.path.expanduser("~") + "/" + dest_file_name
        print("Linking " + src + " to " + dest + ".")

        if os.path.isfile(dest):
            print("Skipping " + dest + ", it already exists") 
        else:
            os.symlink(src, dest)


def link_all():

    with open("../dotfiles/dotfiles.yaml", 'r') as stream:
        modules = yaml.load(stream)

    link_module("default")

    for module in modules["modules"]:
        link_module(module)


if __name__ == "__main__":
    link_all()

 

       


