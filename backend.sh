#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 [setup] [run]"
  exit
fi;

if [ "$1" == "setup" ]; then
  shift;

  # DB Setup
  cd db/docker || return 1
  docker compose up -d
  cd ..
  echo "Passwort für MYSQL Docker Server (siehe db/docker/docker-compose.yaml)"
  mysql -p --protocol=TCP -u root < create_testdata.sql
  cd ..

  # Back Setup
  cd back || return 1
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  deactivate
  cd ..

fi;

if [ "$1" == "run" ]; then

  source back/.venv/bin/activate
  flask --app back run --debug #--host 0.0.0.0

fi;