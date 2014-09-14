#!/bin/bash
#This runs at shutdown and collects the difference between start and end Epoch.
echo 'Collecting Epoch for shutdown'
DOWN=$(date +%s)

echo 'Reading provided file for start Epoch time'
filename="$1"
while read line
do
    DIFF=$(($DOWN-$line))
    echo 'Outputting Difference of start and stop Epoch values to uptimer-seconds, with a date'
    echo $DIFF 1>> uptimer-seconds.log && date +%F 1>> uptimer-seconds.log
done < $filename
