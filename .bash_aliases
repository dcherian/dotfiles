alias ls='ls --color'
alias ll="exa -al"
alias matlab="/usr/local/MATLAB/R2018a/bin/matlab"
alias matlab.2017a='/usr/local/bin/matlab'

alias o="exo-open"

alias epy="jupyter qtconsole --existing=emacs-default.json"
alias ipy="jupyter qtconsole --existing"

alias ncdump='/usr/bin/ncdump'
alias nc-config='/usr/bin/nc-config'

alias e='f -e emacsclient'
alias fr='f -e FoxitReader'
alias fo='filename=`find ~/p/ -type f -printf "%P\n" | fzf`; FoxitReader "/home/deepak/p/$filename" &'
alias mo='filename=`find ~/p/ -type f -printf "%P\n" | fzf`; mupdf "/home/deepak/p/$filename" &'