from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.users.models import User


def is_an_available_username(username):
    """
    Verify if an username is available.

    :username: a string object
    :returns: True or False

    """

    return True if User.query.filter(User.username == username).count() else False


def get_all_users():
    """
    Get all users info. Accepts specify an username.

    :username: a string object
    :returns: a dict with the operation result

    """
    # filter(User.username.like('%rafa%')).all()
    users = User.query.all()

    return users


def get_user_by_username(username=None):
    """
    Get user info by username

    :username: a string object
    :returns: a user object
    """
    user = None
    try:
        user = User.query.filter(User.username == username).one()
    except NoResultFound:
        # TODO: log exceptions
        pass

    return user


def get_user_by_id(user_id=None):
    """
    Get user info by id

    :username: a string object
    :returns: a user object
    """
    user = None
    try:
        user = User.query.filter(User.id == user_id).one()
    except NoResultFound:
        # TODO: log exceptions
        pass

    return user


def create_user(username, password, email):
    """
    Creates an user.

    :username: a string object
    :password: a string object (plaintext)
    :user_id: a str object. Indicates an update.
    :returns: a dict with the operation result

    """

    if is_an_available_username(username) is False:
        # TODO: create custom exceptions
        return {'error': 'The user {!r} already exists.'.format(username)}

    try:
        User(username=username, password=password, email=email).save()
    except Exception as e:
        return {'error': 'Error during the operation: {}'.format(e)}

    return {'created': 'Created the user {!r}.'.format(username)}


def update_user(user_id):
    """
    Creates an user.

    :username: a string object
    :password: a string object (plaintext)
    :user_id: a str object. Indicates an update.
    :returns: a dict with the operation result

    """

    try:
        # TOTO: create update user function
        pass
    except Exception as e:
        return {'error': 'Error during the operation: {}'.format(e)}

    return {'created': 'Update the user {!r}.'.format(user_id)}


def delete_user(user_id):
    """
    Delete an user by user id.

    :user_id: a int object
    :returns: a dict with the operation result

    """
    try:
        user = User.query.get(user_id)
        user.delete()
    except NoResultFound:
        return {'error': 'Invalid user id.'}
    return {'deleted': 'User deleted'}
