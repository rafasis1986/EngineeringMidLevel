#!/bin/sh
python manage.py db migrate
python manage.py db upgrade
python manage.py create_admin
/usr/local/bin/gunicorn -b 0.0.0.0:5000 manage:app &
