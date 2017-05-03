REPOSITORY=/media/deepak/osu-backup-1/backup/

# export BORG_PASSPHRASE='gxz!0lopmacbookborgbackup'
export BORG_PASSPHRASE=''

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
     --keep-daily=7 --keep-weekly=4 --keep-monthly=6
