dotfiles-manager
========
This is my dotfiles management suite.  It is simple and opinionated.  

It allows you to:

1. Keep all your dotfiles in one place.
2. Symlink them anywhere in your home directory.
3. Split them into modules (different dirs in ~/.dotfiles).
4. Only symlink a subset (testing a new configuration?  Only using a subset of your normal dotfiles setup on this machine?).
5. Easily reverse the process and remove all the symlinks that you just created.

Enjoy.


##Getting Started

Clone into ~/.dotfiles-manager:
```
git clone https://github.com/nckturner/dotfiles-manager.git ~/.dotfiles-manager
```

You may want to look at my dotfiles repository to see how it needs to be structured.  You may clone it too:
```
git clone https://github.com/nckturner/dotfiles.git ~/dotfiles
```

##Dotfiles structure

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
   | |-go.sh
   | |-module.yaml
   |-vim
     |-vimrc
     |-module.yaml
```

### link_files.py
This script must be run to create the necessary symlinks from your .dotfiles repository to your $HOME directory.  It will tell you what it finds and successfully links and what it skipped due to links already being present.  

### dotfiles.yaml
This files must be present in the root of `~/.dotfiles`, it tells `link_files.py` which "modules" (based on directory name) to use. 
Example:
```yaml
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
```yaml
files:
  vimrc: .vimrc
```
Another example for my golang configuration:
```yaml
files:
  go.sh: .config/rc.d/go.sh
```

## Note about dotfiles repository:
It should be noted that my zshrc looks like the following, which allows me to use any number of .zsh/.sh source files for my shell configuration, which in turn allows me to keep it organized by keeping it in separate modules in my .dotfiles repository.  Otherwise, I would have to put shell configuration that is specific to, say, ruby, (which should go in the ruby module) into the zsh module to get it in the .zshrc file.  

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
As long as my symlink goes inside `.config/rc.d/` or `/.config/zshrc.d/` then my zshrc file will pick it up.  
