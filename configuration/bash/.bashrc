# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='\[\033[00m\][\[\033[37m\]\u@\h \[\033[33m\]\W\[\033[00m\]]\$ \[\033[00m\]'
PS2='\[\033[35m\]> \[\033[00m\]'

PATH=$PATH:/tools/Xilinx/Vivado/2023.1/bin
PATH=$PATH:/tools/Xilinx/Vitis/2023.1/bin
PATH=$PATH:/tools/nordic
PATH=$PATH:/tools/nordic/nrf-command-line-tools/bin
PATH=$PATH:/tools/gcc-arm-none-eabi/bin
PATH=$PATH:~/version-control/arch-linux-scripts

export EDITOR="/usr/bin/nvim"
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx

source .bash-aliases
source .bash-functions
