from flaskiwsapp.users.controllers import get_user_by_id, get_user_by_email
from flaskiwsapp.snippets.customApi import DUMMY_ERROR_CODE
from flask_jwt import JWTError
from flask import jsonify


def authenticate(email, password):
    user = get_user_by_email(email)
    if user and user.check_password(password) and user.is_active:
        return user


def identity(payload):
    user_id = payload['identity']
    return get_user_by_id(user_id)


def error_handler(e):
    response_dict = {'data': {}}
    error = {}
    if isinstance(e, JWTError):
        error.update({'status': e.status_code})
        error.update({'title': e.error})
        error.update({'detail': 'Auth Failed: {}'.format(e.description)})
        error.update({'code': DUMMY_ERROR_CODE})
        response_dict['data'] = error
        return jsonify(response_dict), e.status_code, e.headers
