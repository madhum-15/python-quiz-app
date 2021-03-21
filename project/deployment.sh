#!/bin/sh

ssh root@162.222.178.164 <<EOF
  cd project
  git pull
  source /opt/envs/project/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart project
  exit
EOF
