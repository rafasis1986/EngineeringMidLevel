#!/bin/sh
python manage.py db init 
python manage.py db migrate
python manage.py db upgrade
python manage.py create_admin
python manage.py runserver
