from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.snippets.constants import ROLE_CLIENT
from flaskiwsapp.snippets.exceptions.clientExceptions import ClientDoesnotExistsException
from flaskiwsapp.snippets.exceptions.userExceptions import UserExistsException
from flaskiwsapp.users.controllers.userControllers import create_user, append_user_role
from flaskiwsapp.users.models.role import Role
from flaskiwsapp.users.models.user import User


def get_all_clients():
    """
    Get all clients info

    :returns: a dict with the operation result

    """
    return User.query.filter(User.roles.any(Role.name == ROLE_CLIENT)).all()


def get_all_email_clients():
    """
    Get all emails from clients

    :returns: a dict with the operation result

    """
    return User.query.filter(User.roles.any(Role.name == ROLE_CLIENT)).with_entities(User.email).all()


def get_client_by_email(email=None):
    """
    Get client info by email

    :email: a string object
    :returns: a client object
    """
    try:
        client = User.query.filter(User.email == email, User.roles.any(Role.name == ROLE_CLIENT)).one()
    except NoResultFound:
        raise ClientDoesnotExistsException(email)
    return client


def get_client_by_id(client_id=None):
    """
    Get client info by id

    :client_id: a integer object
    :returns: a User object
    """
    try:
        client = User.query.filter(User.id == client_id, User.roles.any(Role.name == ROLE_CLIENT)).one()
    except NoResultFound:
        raise ClientDoesnotExistsException(client_id)
    return client


def create_client(email, password=None):
    """
    Create a client.

    :email: a str object. Indicates an update.
    :password: a string object (plaintext)
    :returns: a dict with the operation result
    """
    client = None
    try:
        client = create_user(email, password)
        client = append_user_role(client.id, ROLE_CLIENT)
    except IntegrityError:
        raise UserExistsException(email)
    return client
