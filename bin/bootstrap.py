#!/usr/bin/python
# bootstap.py
#
# Checks dotfiles installation and 
import check_deps

dotfile_manager_root = "$HOME/.dotfiles-manager"
dotfiles = dotfile_manager_root + "/dotfiles"
modules_conf = dotfiles + "/modules.yaml"
zsh_sourcefile = dotfile_manager_root + "/bin/sourcefile.zsh"


def check_installation():
    # TODO check modules if not
    
    #if not check_deps_installed():
        
    #if [[ ! -d $dotfile_manager_root ]] {
    #    print "Dotfiles was not installed correctly.  "
    #    print "Be sure to install it in " + dotfile_manager_root + "."
    #    exit 1
    #}
    pass
