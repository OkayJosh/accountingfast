#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput


python manage.py makemigrations
python manage.py migrate

gunicorn accounting.wsgi:application --bind 0.0.0.0:8000 --log-level info --timeout 180  --workers 3
