# Back-End

This python project was maked using cookiecutter template

```
cookiecutter https://github.com/on3iro/cookiecutter-flask.git
```

## Currently integrated:
* Password hashing via Flask-Bcrypt
* bpython shell
* Testing with pytest, WebTest and pytest-flask
* Test coverage via coverage and pytest-cov
* Flask-Admin
* Login management with Flask-Login
* Database migrations via Flask-Migrate
* Flask-SQLAlchemy
* Formhandling with Flask-WTF
* psycopg2 for postgre connections
* simple login and user registration
* sphinx for documentation
* Implement Flask-RESTful
* Serialize responses with marshmallow-jsonapi
* Disable CORS with Flask-Cors
* Token authentication with Flask-JWT
* sending emails with sendgrid
* Integration test with Travis

## Installation

Install requirements for production or development:

```pip install -r requirements/prod.txt```

or

```pip install -r requirements/dev.txt```

Create your database, make an initial migration and create a default admin
user, follow these commands:

    ./manage.py db init
    ./manage.py db migrate
    ./manage.py db upgrade
    ./manage.py create_admin

## Running the server
    
    ./manage.py server

## Testing the application

    ./manage.py test

## Generating test coverage information

    py.test --cov=<app_name> --cov-report=html


## Create documentation
Simply cd into the ```doc/```-directory and use these commands:

```sphinx-apidoc -f -o source/ ../<YOUR_APP_DIR>```

```make html```


Rafael Torres
rdtr.sis@gmail.com
