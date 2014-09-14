#!bin/bash
#This runs at boot to collect the starting Epoch
echo 'Collecting start Epoch'
date +%s >> /home/member/c/chris/dev/uptimer/uptimer-start.log
