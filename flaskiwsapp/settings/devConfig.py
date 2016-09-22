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
    DB_PATH = os.path.join(BaseConfig.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
