#!/bin/bash

netstat -plant | grep 8001
if [ $? != 0 ]; then
nohup python3.7 manage.py runserver 0.0.0.0:8001 &
sleep 30
exit 0
else
echo "Application already running"
fi
