from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.projects.models.request import Request
from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flaskiwsapp.snippets.exceptions.requestExceptions import RequestDoesnotExistsException


def get_all_requests():
    """
    Get all requests info

    :returns: a dict with the operation result

    """
    # filter(Request.email.like('%rafa%')).all()
    return Request.query.all()


def get_request_by_id(request_id=None):
    """
    Get request info by id

    :request_id: a integer object
    :returns: a request object
    """
    try:
        request = Request.query.get(request_id)
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    return request


def update_request(request_id, kwargs):
    """
    Creates an request.

    :request_id: a integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: request updated

    """
    try:
        target = Request.query.get(request_id)
        target.update(**kwargs)
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    except Exception as e:
        raise BaseIWSExceptions(arg=e.arg[0])
    return target


def delete_request(request_id):
    """
    Delete an request by id.

    :request_id: a int object
    :returns: boolean
    """
    try:
        Request.query.get(request_id).delete()
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    return True
