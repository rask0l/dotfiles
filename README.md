dotfiles-manager
========

This is my dotfiles management suite.  It is simple and opinionated when it can be, and customizable when it must be.  

Enjoy.


Getting Started
---------------

Clone into ~/.dotfiles-manager:
```
git clone https://github.com/nckturner/dotfiles-manager.git ~/.dotfiles-manager
```

You may want to look at my dotfiles repository to see how they need to be structured.  You may clone it:
```
git clone https://github.com/nckturner/dotfiles.git ~/dotfiles.git
```

Dotfiles structure
---------------

The dotfiles repository must be a sibling to the dotfiles manager.  The overall structure looks like this:

```
~ 
 |-.dotfiles-manager
 | |-bin
 |   |-link_files.py
 | 
 |-.dotfiles
   |-dotfiles.yaml
   |-zsh
   | |-zshrc
   | |-module.yaml
   |-default
   |-go
     |-go.sh
     |-module.yaml

### link_files.py
This script must be run to create the necessary symlinks from your .dotfiles repository to your $HOME directory.  It will tell you what it finds and successfully links and what it skipped due to links already being present.  

### dotfiles.yaml
This files must be present in the root of the .dotfiles repository, it tells link files which "modules" (based on directory name) to use. 
Example:
```
modules:
  - vim
  - zsh
  - git
  - go
  - k8s
  - bspwm
  - byobu
```

### module.yaml
Each module has a module.yaml file which states which file should go where.  The following vim/module.yaml file states that the vimrc file should go in $HOME directory (it must be $HOME or a child of $HOME) and the symlink should be named `.vimrc`.
Example:
```
files:
  vimrc: .vimrc
```
Another example for my golang configuration:
```
files:
  go.sh: .config/rc.d/go.sh
```

## Note about dotfiles repository:
It should be noted that my zshrc looks like the following, which allows me to use any number of source files for my shell configuration, which in turn allows me to keep it organized by keeping it in separate files (organized into modules in this repository).  

```
# .zshrc

# Load all files from .config/zshrc.d directory
if [ -d $HOME/.config/zshrc.d ]; then
  for file in $HOME/.config/zshrc.d/*.zsh; do
    source $file
  done
fi

# Load all files from .config/rc.d directory
if [ -d $HOME/.config/rc.d ]; then
  for file in $HOME/.config/rc.d/*.sh; do
    source $file
  done
fi
```
As long as my symlink goes to `.config/rc.d/` or `/config/zshrc.d/` then my zshrc file will pick it up.  
