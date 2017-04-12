#!/usr/bin/env bash

if [ "$1" == "-b" ]; then
    docker build -t parseville .
fi

SOURCE_VOLUME="/home/marty/Projects/Parseville/src"
STATIC_VOLUME="/home/marty/Projects/Parseville/src/collect_static"
NGINX_VOLUME="/home/marty/Projects/Parseville/config/nginx"

if [ "$2" == "-p" ]; then
    SOURCE_VOLUME="/root/Parseville/src"
    STATIC_VOLUME="/root/Parseville/src/collect_static"
    NGINX_VOLUME="/root/Parseville/config/nginx"
fi

echo $SOURCE_VOLUME

docker run -d --name parseville -v $SOURCE_VOLUME:/code parseville
docker run -d --name pnginx -p 8001:8000 --link parseville:web -v $STATIC_VOLUME:/usr/share/nginx/html -v $NGINX_VOLUME:/etc/nginx/conf.d -d nginx