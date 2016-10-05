'''
Created on Sep 22, 2016

@author: rtorres
'''
import os

from flaskiwsapp.settings.baseConfig import BaseConfig


class DevConfig(BaseConfig):
    """Development configuration"""
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    AUTH0_CALLBACK_URL = 'http://localhost/auth/callback'
    AUTH0_CLIENT_ID = ''
    AUTH0_CLIENT_SECRET = ''
    AUTH0_DOMAIN = ''
    APP_DOMAIN = 'localhost'
    APP_URL = 'http://%s' % APP_DOMAIN
    SERVER_NAME = 'locahost'

