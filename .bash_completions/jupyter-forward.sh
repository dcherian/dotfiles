_jupyter_forward_completion() {
    local IFS=$'
'
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _JUPYTER_FORWARD_COMPLETE=complete_bash $1 ) )
    return 0
}

complete -o default -F _jupyter_forward_completion jupyter-forward