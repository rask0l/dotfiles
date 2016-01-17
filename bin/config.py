#!/usr/bin/python

from os.path import expanduser

home = expanduser("~") + "/"
dm_dir = home + ".dotfiles-manager/"
dotfiles_dir = home + ".dotfiles/"
dotfiles_conf = dotfiles_dir + "dotfiles.yaml"

green = "\033[1;32m"
red = "\033[1;31m" 
crimson = "\033[1;31m"
color_end = "\033[1;m"
