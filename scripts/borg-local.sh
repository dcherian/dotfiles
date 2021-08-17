# REPOSITORY=/media/osu-backup-1/backup/
REPOSITORY=/media/deepak/passport/backup/

export BORG_PASSPHRASE=''

export BORG_RELOCATED_REPO_ACCESS_IS_OK=yes

# Backup all of /home and /var/www except a few
# excluded directories
borg create -v --compression lz4 --stats \
     $REPOSITORY::'{now:%Y-%m-%d}'  \
     /home/deepak/

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. The '{hostname}-' prefix is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.
borg prune -v --list $REPOSITORY  \
     --keep-daily=30 --keep-weekly=6 --keep-monthly=10

notify-send -i info "borg-local: finished backing up!"
