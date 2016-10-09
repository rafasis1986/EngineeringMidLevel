# Requirements

- Ubuntu 16.04
- Python 3.5
- Flask  0.11.1
- SqlAlchemy 1.0.15
- Postgres 9.4
- Knockout 3.4
- Durandal 2.1
- Bootstrap 3.3.7
- Typescript 2.0.3
- Docker 1.12.1
- Docker-Compose 1.8.1
- Travis
- Sphinix
- Auth0
- Twilio
- Sendgrid
- Celery

## Origins

Originally i started developing from two templates

```
1 - cookiecutter https://github.com/on3iro/cookiecutter-flask.git

2 - yo durandal2
```

## Download

Clone the repo:

```
git clone https://github.com/rafasis1986/EngineeringMidLevel.git
```


## Setting BE application

Make the enviroment file in the main path:

```
$ vim .env 


And add the fields:

# PostgreSQL
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_USER=your_postgres_user

# Flask app
IWS_BE=prod
FLASK_APP=manage
```

Later settings with your values into Back-End application:

```
$ vim flaskiwsapp/settings/productionConfig.py

...
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://POSTGRES_USER:test@POSTGRES_PASSWORD:5432/POSTGRES_USER'
    SERVER_NAME= 'your_domain'
    AUTH0_CALLBACK_URL = 'http://%s/auth/callback' % (SERVER_NAME)
    AUTH0_CLIENT_ID = 'your_auth0_client_id'
    AUTH0_CLIENT_SECRET = 'your_auth0_client_secret'
    AUTH0_DOMAIN = 'your_auth0_domain'
    APP_URL = 'http://web.your_domain'
    TWILIO_SID = 'your_twilio_sid'
    TWILIO_TOKEN = 'your_twilio_token'
    TWILIO_PHONE = 'your_twilio_phone_number'
    SENDGRID_EMAIL = 'your_email'
    SENDGRID_TOKEN = 'sendgrid_email_token'

```

Remember setting the auth0 callback url in https://auth0.com/

Twilio is a SMS provider, I use this provider because this let me create a free account, 
to send emails i used sendgrid service go to https://sendgrid.com , 
in other hand i used a external queue service from https://www.cloudamqp.com and 
finally to watch the logs you can move to https://rdtr.loggly.com/login and login with 
login **admin** and password **Admin123**



## Setting FE application

Open the environment file and customize with your settings

```
$ vim knockoutapp/app/constants/enviroment.ts

... 
export class Constant {
    public static get AUTH_LABEL(): string { return 'Authorization'; };
    public static get AUTH_PATH(): string { return '/auth'; };
    public static get CHARACTER_PARTITION(): string { return '\\073'; };
    public static get CLIENTS_API(): string { return 'client_list'; };
    public static get DEFAULT_AUTH_URL(): string { return 'http://your_domain/auth'; };
    public static get DEVELOPMENT_ENV(): string { return 'dev'; };
    public static get DEVELOPMENT_BE_URL(): string { return 'http://localhost:5000'; };
    public static get ENV_LABEL(): string { return 'Env'; };
    public static get PAGINATE_LIMIT(): number { return 10; };
    public static get PRODUCTION_ENV(): string { return 'prod'; };
    public static get PRODUCTION_BE_URL(): string { return 'http://your_domain'; };
    public static get REQUESTS_API(): string { return 'request_list'; };
    public static get TICKETS_API(): string { return 'tickets_list'; };
    public static get TYPE_TOKEN(): string { return 'Bearer'; };
    public static get USERS_API(): string { return 'user_list'; };
    public static get USERS_API_ME(): string { return 'me'; };
    public static get URLS_LABEL(): string { return 'urls'; };
}


```

It is important that both applications share the same web domain, 
because when you login a cookie is sent from the BE.

Note: To the current test I used the subdomain **"web"** for the Front-End application, 
personally i wanted add "api" subdomain for the Back-End application, however some 
Flask packages do not let me assign the subdomain

## Deploying with docker-compose

you need install docker and docker-compose

https://docs.docker.com/engine/installation/linux/ubuntulinux/

https://docs.docker.com/compose/install/

When you have the previous pre-requirements, from the main folder project
build your containers with

```
$ docker-compose build
```

Later you can deploy the application with:

```
$ docker-compose up
```

If you want that the containers run as daemon add **-d** to previous sentence 

To show the states from your containers use

```
$ docker-compose ps
```

finally to stop and restart your containers

```
$ docker-compose stop

$ docker-compose start

```

## Starting with the application

To Access at the admin application, go for the url **htpp://your_domain/admin**,
by default the acces protocols are:

**Login:** *admin@example.com*

**Password:** *admin*

With Admin application you can create users, clients, requests and tickets

**User** is the main role in the system, he need be activated and only the 
admin users can access to admin application.
 
**Client** is the person that sends requests to the Users.

**Request** are the main model of the system, they have target_date, 
ticket_url and more information provided by the clients.

**Ticket** is a record to track the user actions, when they checked a request


Now you can acces to the application from

```
http://your_domain
```

You can acces with your *github* or *gmail* account or with a email and password

