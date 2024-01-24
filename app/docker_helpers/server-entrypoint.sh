#!/bin/sh

do cd /app
    echo "Waiting for server volume..."
done


until alembic upgrade head
do
    echo "Waiting for db to be ready..."
    sleep 2
done



# python manage.py createsuperuser --noinput

#gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

gunicorn -w 4 -b 0.0.0.0:8000  main:app --preload