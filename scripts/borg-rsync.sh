#!/bin/sh
REPOSITORY=rsync:darya

# export BORG_PASSPHRASE='gxz!0lopmacbookborgbackup'
export BORG_PASSPHRASE='gxz!0lopborgdarya'

# Backup all of /home and /var/www except a few
# excluded directories
borg create --remote-path=borg1 -v --stats \
     $REPOSITORY::'{now:%Y-%m-%d}'  \
     /home/deepak/website \
     /home/deepak/Documents \
     /home/deepak/org \
     /home/deepak/notes \
     /home/deepak/dotfiles \
     /home/deepak/zotero \
     /home/deepak/ebooks \
     /home/deepak/tools \
     /home/deepak/python \
     /home/deepak/wedding \
     /home/deepak/dotfiles

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. The '{hostname}-' prefix is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.
borg prune --remote-path=borg1 -v --list $REPOSITORY  \
     --keep-daily=7 --keep-weekly=4 --keep-monthly=6

notify-send -i info "borg-rsync: Finished backing up!"
