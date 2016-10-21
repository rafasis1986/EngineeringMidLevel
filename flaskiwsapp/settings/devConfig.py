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
    SQLALCHEMY_DATABASE_URI = 'postgresql://docker:docker@localhost:15432/iws'
    SERVER_HOST = "localhost:5000"
    AUTH_SUBDOMAIN = 'auth'
    AUTH0_CALLBACK_URL = 'http://%s/auth/callback' % (SERVER_HOST)
    AUTH0_CALLBACK_EMP_URL = 'http://%s/auth/callback/emp' % (SERVER_HOST)
    AUTH0_CLIENT_ID = 'zGHCpFfHqzObUpR006g3RvD4AOu0wJqF'
    AUTH0_CLIENT_SECRET = '8oKf3JBCFExlt8eJzUpWdH_4B3kbfQx8tC_o0UcuwSTr6PbkfUr5QZOVYGz0LcHx'
    AUTH0_DOMAIN = 'rtorres.auth0.com'
    APP_DOMAIN = 'localhost:9000'
    APP_URL = 'http://%s' % APP_DOMAIN
    CELERY_BROKER_URL = 'amqp://oghhwozm:E50Pt5-Qua-k_uIestJZ0_wylZVmGzYF@wildboar.rmq.cloudamqp.com/oghhwozm'
    CELERY_IMPORTS = ('flaskiwsapp.workers.sms', 'flaskiwsapp.workers.emails')
    TWILIO_SID = 'AC0ad3813a644ee7083fab4e40766c701e'
    TWILIO_TOKEN = '3dc30c519903dfc1c9ed0b643dead75d'
    TWILIO_PHONE = '+17609786395'
    SENDGRID_EMAIL = 'rdtr.sis@gmail.com'
    SENDGRID_TOKEN = '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'
    CACHE_DEFAULT_TIMEOUT = 120
    CACHE_TYPE = 'simple'
