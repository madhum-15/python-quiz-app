#!/bin/bash

netstat -plant | grep 8001 | grep Listen
if [ $? != 0 ]; then
python3.7 manage.py runserver 0.0.0.0:8001
exit 0
else
echo "Application already running"
fi
