FROM python:3.8-slim

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT


# install psycopg2
RUN apt-get update \
 && apt-get -y install gcc python3-dev musl-dev \
 && apt-get -y install postgresql-server-dev-all \
 && pip install psycopg2

# RUN pip install virtualenv && virtualenv -p python /app/venv
# COPY requirements.txt requirements.txt
# RUN /app/venv/bin/pip install -r requirements.txt


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add and run as non-root user
# RUN adduser myuser
# USER myuser


COPY . .
# RUN /app/venv/bin/

# run gunicorn
# CMD gunicorn accounting.wsgi:application --bind 0.0.0.0:$PORT
# CMD chmod +x manage.py
# CMD python manage.py runserver 0.0.0.0:8000
CMD gunicorn accounting.wsgi:application --bind 0.0.0.0:8000 --log-level info --timeout 180  --workers 3