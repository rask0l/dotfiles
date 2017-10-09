dotm
========
This is my dotfiles management suite.  It is simple and opinionated.  

It allows you to:

1. Keep all your dotfiles in one place.
2. Symlink them anywhere in your home directory.
3. Split them into modules (different dirs in ~/.dotfiles).
4. Use profiles to choose which modules to use on a certain machine.
5. Easily reverse the process and remove all the symlinks that you just created.

Enjoy.


## Getting Started

Clone into ~/.dotm:
```
git clone https://github.com/nckturner/dotm.git ~/.dotm
```

You may want to look at my dotfiles repository to see how it needs to be structured.  You may clone it too:
```
git clone https://github.com/nckturner/dotfiles-example.git ~/.dotfiles
```

## Dotfiles structure

The dotfiles repository must be a sibling to the dotfiles manager.  The overall structure looks like this:

```
~ 
 |-.dotm
 | |
 | |-bin
 |   |-link_files.py
 | 
 |-.dotfiles
   |
   |-modules
   | |
   | |-zsh
   | | |-zshrc
   | | |-module.yaml
   | |
   | |-go
   | | |-go.sh
   | | |-module.yaml
   | |
   | |-vim
   |   |-vimrc
   |   |-module.yaml
   |
   |-profiles
     |-profile1
       |-test
       |-profile.yaml
       |-profile1.sh
```

### bin/dotm.py
This script must be run to create the necessary symlinks from your .dotfiles repository to your $HOME directory.  It will tell you what it finds and successfully links and what it skipped due to links already being present.  

### profile.yaml
This file must be present in each profile directory in `~/.dotfiles/profiles/`, it determines which modules each profile will use.  It can also have its own dotfiles, outside of any modules.

Example:

```yaml
modules:
  - vim
  - zsh
  - git
  - go
  - bspwm
links:
  profile: .profile
  gitconfig: .gitconfig
```

### module.yaml
Each module has a module.yaml file which states which file should be symlinked where.  

The following vim/module.yaml file states that the vimrc file should go in $HOME directory and the symlink be named `.vimrc` (the path is always relative to $HOME, so it must be $HOME or a child of $HOME).
Example:

```yaml
files:
  vimrc: .vimrc
```
Another example for a golang configuration:

```yaml
files:
  go.sh: .config/rc.d/go.sh
```

### test
A test script must be in each profile.  Dotm uses the test file to determine which profile to choose.  `test` should be an executable file that returns 0 on the computer(s) that it should be used on.  For example, it could do a string comparison against the hostname, or the architecture, or a value in `/etc/os-release`.  An example test file in a "homepc" profile could be `~/.dotfiles/profiles/homepc/test`:

```bash
#!/bin/bash

if [[ "$(hostname)" = "myhomepc" ]]; then
	exit 0
else
	exit 1
fi
```

## Note about dotfiles repository:
My zshrc looks like the following: 

```zsh
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

For any shell configuration, I create symlinks pointing to module files inside `~/.config/rc.d/` or `~/.config/zshrc.d/` and my zshrc file will pick it up.  This allows me to keep, for example, ruby shell configuration in my ruby module (~/.dotfiles/modules/ruby/ruby.zsh), and go shell configuration in my go module (~/.dotfiles/modules/go/go.zsh), rather than putting everything in my .zshrc file which would defeat the whole purpose of this module system.  The same concept could be followed with `.bashrc` or `.profile`.
