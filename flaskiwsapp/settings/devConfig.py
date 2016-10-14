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
    SQLALCHEMY_DATABASE_URI = 'postgresql://test:test@localhost:5432/iws3'
    SERVER_HOST = "localhost:5000"
    AUTH_SUBDOMAIN = 'auth'
    AUTH0_CALLBACK_URL = 'http://%s/auth/callback' % (SERVER_HOST)
    AUTH0_CLIENT_ID = 'zGHCpFfHqzObUpR006g3RvD4AOu0wJqF'
    AUTH0_CLIENT_SECRET = '8oKf3JBCFExlt8eJzUpWdH_4B3kbfQx8tC_o0UcuwSTr6PbkfUr5QZOVYGz0LcHx'
    AUTH0_DOMAIN = 'rtorres.auth0.com'
    APP_DOMAIN = 'localhost:9000'
    APP_URL = 'http://%s' % APP_DOMAIN
    CELERY_BROKER_URL = 'amqp://tathtgvg:FKo6F3svJg0QfSbLRbd7rGdj93gTh3TY@reindeer.rmq.cloudamqp.com/tathtgvg'
    CELERY_IMPORTS = ('flaskiwsapp.workers.sms', 'flaskiwsapp.workers.emails')
    TWILIO_SID = 'AC0ad3813a644ee7083fab4e40766c701e'
    TWILIO_TOKEN = 'd0bfb91cd04e1e9cd2bffb12edee752e'
    TWILIO_PHONE = '+17609786395'
    SENDGRID_EMAIL = 'rdtr.sis@gmail.com'
    SENDGRID_TOKEN = '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'
