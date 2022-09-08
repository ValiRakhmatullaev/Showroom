#!/bin/sh


python manage.py collectstatic

python manage.py makemigrations
python manage.py migrate
gunicorn config.wsgi:aplication --blind 0.0.0.0:8000
