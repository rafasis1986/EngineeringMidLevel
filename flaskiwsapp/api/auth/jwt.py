from flaskiwsapp.users.controllers import get_user_by_id, get_user_by_email


def authenticate(email, password):
    user = get_user_by_email(email)
    if user and user.check_password(password) and user.is_active:
        return user


def identity(payload):
    user_id = payload['identity']
    return get_user_by_id(user_id)


def error_handler(error):
    return 'Auth Failed: {}'.format(error.description), 400
