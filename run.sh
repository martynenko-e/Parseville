#!/usr/bin/env bash

if [ "$1" == "-b" ]; then
    docker build -t parseville .
fi

SOURCE_VOLUME="/Users/yevhenmartynenko/_projects/Parseville/src"
STATIC_VOLUME="/Users/yevhenmartynenko/_projects/Parseville/src/collect_static"
NGINX_VOLUME="/Users/yevhenmartynenko/_projects/Parseville/config/nginx"
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




# if [ "$1" == "-b" ]; then
#     docker build -t parseville .
# fi

# SOURCE_VOLUME="/home/marty/Projects/Parseville/src"
# STATIC_VOLUME="/home/marty/Projects/Parseville/src/collect_static"
# NGINX_VOLUME="/home/marty/Projects/Parseville/config/nginx"
# EXPOSE_PORT=8001

# if [ "$2" == "-p" ]; then
#     SOURCE_VOLUME="/root/Parseville/src"
#     STATIC_VOLUME="/root/Parseville/src/collect_static"
#     NGINX_VOLUME="/root/Parseville/config/nginx"
#     EXPOSE_PORT=8000
# fi

#docker run -d --name nginx-proxy -p 80:80 --net reverse-proxy -v /var/run/docker.sock:/tmp/docker.sock:ro  -v $STATIC_VOLUME:/usr/share/nginx/html jwilder/nginx-proxy
#docker run -d --name parseville --net reverse-proxy -v /root/Parseville/src:/code parseville
#docker run -d --name nginx --link parseville:web --net reverse-proxy -e "VIRTUAL_HOST=parse-it.in.ua,www.parse-it.in.ua" -v $STATIC_VOLUME:/usr/share/nginx/html -v $NGINX_VOLUME:/etc/nginx/conf.d -d nginx

#docker run -d -p 80:80 -p 443:443 \
#    --name nginx-proxy \
#    --net reverse-proxy \
#    -v $HOME/certs:/etc/nginx/certs:ro \
#    -v /etc/nginx/vhost.d \
#    -v /usr/share/nginx/html \
#    -v /var/run/docker.sock:/tmp/docker.sock:ro \
#    --label com.github.jrcs.letsencrypt_nginx_proxy_companion.nginx_proxy=true \
#    jwilder/nginx-proxy

#docker run -d \
#    --name nginx-letsencrypt \
#    --net reverse-proxy \
#    --volumes-from nginx-proxy \
#    -v $HOME/certs:/etc/nginx/certs:rw \
#    -v /var/run/docker.sock:/var/run/docker.sock:ro \
#    jrcs/letsencrypt-nginx-proxy-companion

#docker run -d --name parseville --net reverse-proxy -v /root/Parseville/src:/code parseville

# docker run -d --name nginx \
#     --link parseville:web \
#     --net reverse-proxy \
#     -e 'LETSENCRYPT_EMAIL=clericmart@gmail.com' \
#     -e 'LETSENCRYPT_HOST=parse-it.in.ua' \
#     -e "VIRTUAL_HOST=parse-it.in.ua,www.parse-it.in.ua" \
#     -v $STATIC_VOLUME:/usr/share/nginx/html \
#     -v $NGINX_VOLUME:/etc/nginx/conf.d -d nginx


# docker run -d --restart always \
# --net reverse-proxy -e 'LETSENCRYPT_EMAIL=clericmart@gmail.com' \
# -e 'LETSENCRYPT_HOST=blog.parse-it.in.ua,www.blog.parse-it.in.ua' \
# -e "VIRTUAL_HOST=blog.parse-it.in.ua,www.blog.parse-it.in.ua" \
# --name temy -v /root/temy-test/src:/src django11