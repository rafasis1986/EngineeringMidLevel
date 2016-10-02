from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flaskiwsapp.snippets.exceptions.clientExceptions import ClientDoesnotExistsException, \
    ClientExistsException
from flaskiwsapp.users.models.client import Client


def is_an_available_email(email):
    """
    Verify if an email is available.

    :email: a string object
    :returns: True or False

    """
    return True if Client.query.filter(Client.email == email).count() else False


def get_all_clients():
    """
    Get all clients info

    :returns: a dict with the operation result

    """
    # filter(Client.email.like('%rafa%')).all()
    return Client.query.all()


def get_client_by_email(email=None):
    """
    Get client info by email

    :email: a string object
    :returns: a client object
    """
    try:
        client = Client.query.filter(Client.email == email).one()
    except NoResultFound:
        raise ClientDoesnotExistsException(email)
    return client


def get_client_by_id(client_id=None):
    """
    Get client info by id

    :client_id: a integer object
    :returns: a client object
    """
    try:
        client = Client.query.get(client_id)
    except NoResultFound:
        raise ClientDoesnotExistsException(client_id)
    return client


def create_client(email, password=None):
    """
    Creates an client.

    :email: a str object. Indicates an update.
    :password: a string object (plaintext)
    :returns: a dict with the operation result
    """
    client = None
    try:
        client = Client(password=password, email=email).save()
    except IntegrityError:
        raise ClientExistsException(email)
    return client


def update_client(client_id, kwargs):
    """
    Creates an client.

    :client_id: a integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: client updated

    """
    try:
        client = Client.query.get(client_id)
        client.update(**kwargs)
    except NoResultFound:
        raise ClientDoesnotExistsException(client_id)
    except Exception as e:
        raise BaseIWSExceptions(arg=e.arg[0])
    return client


def delete_client(client_id):
    """
    Delete an client by client id.

    :client_id: a int object
    :returns: boolean
    """
    try:
        Client.query.get(client_id).delete()
    except NoResultFound:
        raise ClientDoesnotExistsException(client_id)
    return True


def delete_client_by_email(email):
    """
    Delete an client by email.

    :email: a string object
    :returns: boolean
    """
    try:
        Client.query.filter(Client.email == email).one().delete()
    except NoResultFound:
        raise ClientDoesnotExistsException(email)
    return True
