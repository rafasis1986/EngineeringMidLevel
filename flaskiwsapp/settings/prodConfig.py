'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.settings.baseConfig import BaseConfig

class ProdConfig(BaseConfig):
    """Production configuration"""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
