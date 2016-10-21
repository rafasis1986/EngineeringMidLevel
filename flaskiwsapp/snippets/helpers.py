'''
Created on Sep 22, 2016

@author: rtorres
'''
from flask_jwt import JWT, current_identity, JWTError

from flaskiwsapp.auth.jwt import authenticate, identity, error_handler
from functools import wraps


def register_token_auth(app):
    token_auth = JWT(app, authenticate, identity)
    token_auth.jwt_error_callback = error_handler
    return token_auth


def is_admin_user(fn):
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        if not current_identity.is_admin:
            raise JWTError('Authorization Required', 'The user does have permission to the request')
        return fn(*args, **kwargs)
    return decorated_function


def roles_required(*role_names):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not current_identity.has_role(*role_names):
                raise JWTError('Authorization Required', 'The user does have permission to the request')
            return func(*args, **kwargs)
        return decorated_view
    return wrapper
