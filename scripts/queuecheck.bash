#!/bin/bash

# cron requires environment variables to be set
export SGE_ROOT=/share/apps/gridengine/62u5_20110621
export SGE_CLUSTER_NAME=scylla
export SGE_CELL=default
export SGE_ARCH=lx-amd64

# cron requires absolute path because environment isn't set
qstat=/share/apps/gridengine/62u5_20110621/bin/lx-amd64/qstat
grep=/bin/grep
awk=/usr/bin/awk
cut=/usr/bin/cut

# parse qstat output. Use GREP instead of -u because that results in a title
# line passing checks. I do not want that
#status=$($QSTAT | $AWK '{print $1, $5}')
# get job numbers that satisfy criterion
#job=$( echo $status | $GREP "\br\|\bS\|\bt\|\bR" | $AWK '{print $1}' )

#job=$($QSTAT | $AWK '{print $1, $5}' | $GREP "\br" | $AWK '{print $1}')
job=$( echo $($qstat | $awk '{print $1, $5}' | $grep "\bt\|\bS\|\bR" | $awk '{print $1}') | $cut -d ' ' -f3-)
# get job name for above job numbers
OUT=$($qstat | $grep "dcherian" | $grep ${job// /\\\|} | $awk '{print $3'})
echo $OUT
# check that cron is working
#DATE=$(date)
#echo "running on cron: $DATE" >> ~/croncheck
#echo "$QSTAT" >> ~/croncheck
#echo $OUT >> ~/croncheck

# if not an empty string then, email OUT to me
if [[ !( -z "$OUT" ) ]]; then
    echo $OUT | mail -s "queuecheck" dcherian@mit.edu
fi