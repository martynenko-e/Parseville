#!/usr/bin/env bash

if [ "$1" == "-b" ]; then
    docker build -t parseville .
fi

SOURCE_VOLUME="/home/marty/Projects/Parseville/src"
STATIC_VOLUME="/home/marty/Projects/Parseville/src/collect_static"
NGINX_VOLUME="/home/marty/Projects/Parseville/config/nginx"
EXPOSE_PORT=8001

if [ "$2" == "-p" ]; then
    SOURCE_VOLUME="/root/Parseville/src"
    STATIC_VOLUME="/root/Parseville/src/collect_static"
    NGINX_VOLUME="/root/Parseville/config/nginx"
    EXPOSE_PORT=8000
fi

echo $SOURCE_VOLUME

docker run -d --name parseville -v $SOURCE_VOLUME:/code parseville
docker run -d --name pnginx -p $EXPOSE_PORT:8000 --link parseville:web -v $STATIC_VOLUME:/usr/share/nginx/html -v $NGINX_VOLUME:/etc/nginx/conf.d -d nginx