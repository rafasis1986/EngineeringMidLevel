import datetime

from flask import current_app

from flaskiwsapp.users.controllers import get_user_by_username, get_user_by_id
from flaskiwsapp.users.models import User


def set_jwt_handlers(jwt):
    """
    Define handlers to jwt.

    :jwt: flask_jwt.JWT object
    :returns: None
    """
    @jwt.authentication_handler
    def authenticate(username, password):
        user = get_user_by_username(username)
        if user and user.check_password(password):
            return user
        return None

    @jwt.authentication_handler
    def authenticate(username, password):
        user = get_user_by_username(username)
        if user and user.check_password(password):
            return user
        return None

    @jwt.error_handler
    def error_handler(error):
        return 'Auth Failed: {}'.format(error.description), 400

    @jwt.payload_handler
    def make_payload(user):
        return {
            'user_id': str(user.id),
            'exp': (datetime.datetime.utcnow() +
                    current_app.config.get('JWT_EXPIRATION_DELTA')).isoformat()
        }

    @jwt.user_handler
    def load_user(payload):
        return get_user_by_id(payload['user_id'])
