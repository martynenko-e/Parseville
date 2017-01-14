#!/usr/bin/env bash


if [ "$1" == "-b" ]; then
    docker build -t parseville .
fi

DB_HOST="192.168.99.100"
DB_NAME="parseville"
DB_USER="root"
DB_PASS="123456"
DB_PORT=3306

#docker run -d --name parseville_db -e MYSQL_ROOT_PASSWORD=$DB_PASS -p 3306:3306 -e MYSQL_USER=docker -e MYSQL_PASSWORD=dokerpass -e MYSQL_DATABASE=$DB_NAME mysql:5.6 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --explicit_defaults_for_timestamp=1 --wait_timeout=60
#docker run -d --name parseville -p 8000:8000 -e DB_HOST=$DB_HOST -e DB_NAME=$DB_NAME -e DB_PORT=$DB_PORT -e DB_USER=$DB_USER -e DB_PASS=$DB_PASS parseville python manage.py runserver 0.0.0.0:8000
#docker run -d --name myadmin -p 8080:80 -e PMA_HOST=$DB_HOST -e PMA_PORT=$DB_PORT phpmyadmin/phpmyadmin

#docker exec -d apilocalizationproxy python manage.py makemigrations ApiLocalizationProxy
#docker exec -d apilocalizationproxy python manage.py migrate
#docker exec apilocalizationproxy python manage.py createsuperuser