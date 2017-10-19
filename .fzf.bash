# Setup fzf
# ---------
if [[ ! "$PATH" == */home/deepak/.fzf/bin* ]]; then
  export PATH="$PATH:/home/deepak/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "/home/deepak/.fzf/shell/completion.bash" 2> /dev/null

# Key bindings
# ------------
source "/home/deepak/.fzf/shell/key-bindings.bash"

