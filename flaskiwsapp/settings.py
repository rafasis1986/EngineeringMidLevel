# -*- coding: utf-8 -*-
"""Application configuration"""
import os

import datetime


class Config(object):
    """Base configuration"""

    # SECRET_KEY = os.environ.get('FLA_SECRET', 'secret-key')  # TODO: Change me
    SECRET_KEY = '\xdaZD\x8d\x96\x1d\x91~4]\xae\xb4R*\x8dYr\x8a\xda\x14\xaf\xc3d\xb1'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_URL_RULE = '/api/auth'
    JWT_EXPIRATION_DELTA = datetime.timedelta(days=1)
    JWT_AUTH_HEADER_PREFIX = 'Bearer'
    API_VERSION = 'v1.0'


class ProdConfig(Config):
    """Production configuration"""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me


class DevConfig(Config):
    """Development configuration"""
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class TestConfig(Config):
    """Test configuratin"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at keast 4 to avoid "Value Error: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
