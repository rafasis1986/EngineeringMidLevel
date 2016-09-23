'''
Created on Sep 22, 2016

@author: rtorres
'''
from flask_jwt import JWT

from flaskiwsapp.auth.jwt import authenticate, identity, error_handler


def register_token_auth(app):
    token_auth = JWT(app, authenticate, identity)
    token_auth.jwt_error_callback = error_handler
    return token_auth
