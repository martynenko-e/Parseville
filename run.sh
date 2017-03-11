#!/usr/bin/env bash


if [ "$1" == "-b" ]; then
    docker build -t parseville .
fi

SOURCE_VALUE="/home/marty/Projects/Parseville/src"

docker run --name parseville -v $SOURCE_VALUE:/code -p 8000:8000 parseville python manage.py runserver 0.0.0.0:8000