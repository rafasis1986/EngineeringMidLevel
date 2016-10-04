'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.settings.baseConfig import BaseConfig


class ProdConfig(BaseConfig):
    """Production configuration"""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://POSTGRES_USER:test@POSTGRES_PASSWORD:5432/POSTGRES_USER'
    SERVER_NAME = 'your_domain'
    AUTH0_CALLBACK_URL = 'http://%s/auth/callback' % (SERVER_NAME)
    AUTH0_CLIENT_ID = 'your_auth0_client_id'
    AUTH0_CLIENT_SECRET = 'your_auth0_client_secret'
    AUTH0_DOMAIN = 'your_auth0_domain'
    APP_URL = 'http://web.your_domain'
