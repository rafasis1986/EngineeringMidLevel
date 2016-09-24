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
    DB_NAME = 'dev.db'
    # Put the db file in project root
    # 'postgresql+psycopg2://databaseuser:P@ssw0rd@localhost/the_database' 
    DB_PATH = os.path.join(BaseConfig.PROJECT_ROOT, DB_NAME)
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    SQLALCHEMY_DATABASE_URI = 'postgresql://test:test@localhost/iws'
    AUTH0_CALLBACK_URL = 'http://auth.test:5000/callback'
    AUTH0_CLIENT_ID = 'zGHCpFfHqzObUpR006g3RvD4AOu0wJqF'
    AUTH0_CLIENT_SECRET = '8oKf3JBCFExlt8eJzUpWdH_4B3kbfQx8tC_o0UcuwSTr6PbkfUr5QZOVYGz0LcHx'
    AUTH0_DOMAIN = 'rtorres.auth0.com'
    APP_URL = 'http://localhost:3000'
    SERVER_NAME = 'test:5000'
