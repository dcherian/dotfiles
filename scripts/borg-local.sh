REPOSITORY=/media/osu-backup-1/backup/

export BORG_PASSPHRASE=''

export BORG_RELOCATED_REPO_ACCESS_IS_OK=yes

# Backup all of /home and /var/www except a few
# excluded directories
borg create --compression lz4 -v --stats \
     $REPOSITORY::'{now:%Y-%m-%d}'  \
     /home/deepak/

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. The '{hostname}-' prefix is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.
borg prune -v --list $REPOSITORY  \
     --keep-daily=14 --keep-weekly=6 --keep-monthly=10
