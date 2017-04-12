#!/usr/bin/env bash


if [ "$1" == "-b" ]; then
    docker build -t parseville .
fi

SOURCE_VOLUME="/home/marty/Projects/Parseville/src"
STATIC_VOLUME="/home/marty/Projects/Parseville/src/collect_static"
NGINX_VOLUME="/home/marty/Projects/Parseville/config/nginx"

docker run -d --name parseville -v $SOURCE_VOLUME:/code parseville
docker run -d --name pnginx -p 8001:8000 --link parseville:web -v $STATIC_VOLUME:/usr/share/nginx/html -v $NGINX_VOLUME:/etc/nginx/conf.d -d nginx