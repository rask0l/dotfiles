dotfiles
========

This is my dotfiles management suite.  It is simple and opinionated when it can be, and customizable when it must be.  

Enjoy.


Getting Started
---------------

Clone dotfiles into ~/.dotfiles:
```
git clone https://github.com/rask0l/dotfiles.git ~/.dotfiles && ~/.dotfiles/bin/bootstrap
```

Adding dotfiles
---------------

Dotfiles must be put in a subfolder of the dotfiles folder.  The name of the subfolder must match the module name in dotfiles/dotfiles.yaml.  
Example dotfiles.yaml file: 

  modules:
    - vim
    - zsh

This means files in `dotfiles/vim` and `dotfiles/zsh` will be symlinked to your home directory, for example:

~/.vimrc -> ~/dotfiles-manager/dotfiles/vim/vimrc
~/.zshrc -> ~/dotfiles-manager/dotfiles/zsh/zshrc


Ignoring dotfiles
-----------------

Todo
