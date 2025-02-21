# If not running interactively, don't do anything
[[ $- != *i* ]] && return

function format_git() {
    if [ $(git rev-parse --is-inside-git-dir 2> /dev/null) ]; then
        branch=$(git branch --show-current)
        if [ -z "$branch" ]; then
            branch=$(git rev-parse --short HEAD)
        fi
        printf " $branch";
    fi
}

style_reset="\[\033[00m\]"
style_user="\[\033[37m\]"
style_directory="\[\033[33m\]"
style_git="\[\033[34m\]"
style_pending="\[\033[35m\]"

PS1="[${style_user}\u@\h ${style_directory}\W${style_git}\$(format_git)${style_reset}]\$ "
PS2="${style_pending}> ${style_reset}"
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
