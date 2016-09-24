from flaskiwsapp.users.controllers import get_user_by_id, get_user_by_email
from flaskiwsapp.snippets.customApi import DUMMY_ERROR_CODE
from flask_jwt import JWTError
from flask import jsonify
from flaskiwsapp.snippets.exceptions.userExceptions import UserDoesnotExistsException
from flask_api.status import HTTP_500_INTERNAL_SERVER_ERROR


def authenticate(email, password):
    try:
        user = get_user_by_email(email)
        if user and user.check_password(password.encode('utf-8')) and user.is_active:
            return user
    except UserDoesnotExistsException as e:
        raise JWTError(error=str(type(e)), description=e.message)


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
    elif isinstance(e, Exception):
        error.update({'status': HTTP_500_INTERNAL_SERVER_ERROR})
        error.update({'title': str(type(e))})
        error.update({'detail': 'Auth Failed: {}'.format(e.args[0])})
        error.update({'code': DUMMY_ERROR_CODE})
        response_dict['data'] = error
        return jsonify(response_dict), e.status_code, e.headers
