#!/usr/bin/python

import config
import os

modules = ["yaml"]

def check_deps_installed():
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(config.red + "- You are missing a dependency: " + module + config.color_end)
            return False
    print(config.green + "+ Dependencies are all installed." + config.color_end)
    return True

def check_dotfiles():
    if os.path.isdir(config.dotfiles_dir):
        print(config.green + "+ The directory: `" + config.dotfiles_dir + "` exists." + config.color_end)
        return True
    else:
        print(config.red + "- The directory: `" + config.dotfiles_dir + "` does not exist." + config.color_end)
        return False

if __name__ == "__main__":
    print("Checking installation...")
    check_deps_installed()
    check_dotfiles()
