'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.settings.baseConfig import BaseConfig


class TestConfig(BaseConfig):
    """Test configuratin"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/iws_test'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at keast 4 to avoid "Value Error: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
