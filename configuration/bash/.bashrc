# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='\[\033[00m\][\[\033[37m\]\u@\h \[\033[33m\]\W\[\033[00m\]]\$ \[\033[00m\]'
PS2='\[\033[35m\]> \[\033[00m\]'

PATH=$PATH:~/version-control/arch-linux-scripts
PATH=$PATH:~/bin

export EDITOR="/usr/bin/nvim"
export MANPAGER="nvim +Man!"
export MANWIDTH=100
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx

source ~/.bash-aliases
source ~/.bash-functions
source ~/.bash-local &> /dev/null
