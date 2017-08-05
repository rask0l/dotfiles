#!/usr/bin/python

from os.path import expanduser, join

home = expanduser("~")
dm_dir = join(home, ".dotm/")
dotfiles_dir = join(home, ".dotfiles")
modules_dir = join(dotfiles_dir, "modules")
profiles_dir = join(dotfiles_dir, "profiles")
module_conf = "module.yaml"

green = "\033[1;32m"
red = "\033[1;31m"
crimson = "\033[1;31m"
color_end = "\033[0;m"
