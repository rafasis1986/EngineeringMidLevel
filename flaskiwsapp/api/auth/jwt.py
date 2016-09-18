from functools import wraps

from flask.helpers import make_response
from flask_jwt import jwt_required, current_identity

from flaskiwsapp.users.controllers import get_user_by_username, get_user_by_id


def authenticate(username, password):
    user = get_user_by_username(username)
    if user and user.check_password(password) and user.is_active:
        return user


def identity(payload):
    user_id = payload['identity']
    return get_user_by_id(user_id)


def error_handler(error):
    return 'Auth Failed: {}'.format(error.description), 400
