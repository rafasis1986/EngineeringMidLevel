from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.users.models.user import User
from flaskiwsapp.snippets.exceptions.userExceptions import UserDoesNotExistsException,\
    UserExistsException
from sqlalchemy.exc import IntegrityError
from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flaskiwsapp.users.controllers.roleControllers import get_role_by_name
from flaskiwsapp.snippets.constants import ROLE_CLIENT


def is_an_available_email(email):
    """
    Verify if an email is available.

    :email: a string object
    :returns: True or False

    """
    return False if User.query.filter(User.email == email).count() else True


def get_all_users():
    """
    Get all users info

    :returns: a dict with the operation result

    """
    # filter(User.email.like('%rafa%')).all()
    return User.query.all()


def get_user_by_email(email=None):
    """
    Get user info by email

    :email: a string object
    :returns: a user object
    """
    try:
        user = User.query.filter(User.email == email).one()
    except NoResultFound:
        raise UserDoesNotExistsException(email)
    return user


def get_user_by_id(user_id=None):
    """
    Get user info by id

    :user_id: a integer object
    :returns: a user object
    """
    try:
        user = User.query.get(user_id)
    except NoResultFound:
        raise UserDoesNotExistsException(user_id)
    return user


def create_user(email, password=None):
    """
    Creates an user.

    :email: a str object. Indicates an update.
    :password: a string object (plaintext)
    :returns: a dict with the operation result
    """
    user = None
    try:
        user = User(password=password, email=email).save()
    except IntegrityError:
        raise UserExistsException(email)
    return user


def update_user(user_id, kwargs):
    """
    Creates an user.

    :user_id: a integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: user updated

    """
    try:
        user = User.query.get(user_id)
        user.update(**kwargs)
    except NoResultFound:
        raise UserDoesNotExistsException(user_id)
    except Exception as e:
        raise BaseIWSExceptions(arg=e.arg[0])
    return user


def update_user_password(user_id, password):
    """
    Creates an user.

    :user_id: a integer object. Indicates an update.
    :password: string object
    :returns: user updated

    """
    try:
        user = User.query.get(user_id)
        user.set_password(password)
        user.save()
    except NoResultFound:
        raise UserDoesNotExistsException(user_id)
    except Exception as e:
        raise BaseIWSExceptions()
    return user


def append_user_role(user_id, role_name):
    """
    Creates an user.

    :user_id: a integer object. Indicates an update.
    :role_name: a string object
    :password: string object
    :returns: user updated

    """
    try:
        user = User.query.get(user_id)
        role = get_role_by_name(role_name)
        user.roles.append(role)
        user.save()
    except NoResultFound:
        raise UserDoesNotExistsException(user_id)
    except Exception as e:
        raise BaseIWSExceptions()
    return user


def delete_user(user_id):
    """
    Delete an user by user id.

    :user_id: a int object
    :returns: boolean
    """
    try:
        User.query.get(user_id).delete()
    except NoResultFound:
        raise UserDoesNotExistsException(user_id)
    return True


def delete_user_by_email(email):
    """
    Delete an user by email.

    :email: a string object
    :returns: boolean
    """
    try:
        User.query.filter(User.email == email).one().delete()
    except NoResultFound:
        raise UserDoesNotExistsException(email)
    return True
