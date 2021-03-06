'''
Created on Sep 22, 2016

@author: rtorres
'''
import os
import datetime


class BaseConfig(object):
    """Base configuration"""
    # SECRET_KEY = os.environ.get('FLA_SECRET', 'secret-key')  # TODO: Change me
    APP_NAME = 'IWS'
    SECRET_KEY = '\xdaZD\x8d\x96\x1d\x91~4]\xae\xb4R*\x8dYr\x8a\xda\x14\xaf\xc3d\xb1'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_URL_RULE = '/api/auth'
    JWT_EXPIRATION_DELTA = datetime.timedelta(days=1)
    JWT_AUTH_HEADER_PREFIX = 'Bearer'
    API_VERSION = 'v1.0'
    CELERY_BROKER_URL = 'amqp://oghhwozm:E50Pt5-Qua-k_uIestJZ0_wylZVmGzYF@wildboar.rmq.cloudamqp.com/oghhwozm'
    CELERY_IMPORTS = ()
    CACHE_DEFAULT_TIMEOUT = 120
    CACHE_TYPE = 'simple'
