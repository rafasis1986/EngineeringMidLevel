from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.projects.models.request import Request
from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flaskiwsapp.snippets.exceptions.requestExceptions import RequestDoesnotExistsException


def get_all_requests():
    """
    Get all requests info

    :returns: a dict with the operation result

    """
    return Request.query.order_by(Request.id).all()


def get_all_client_requests(client_id):
    """
    Get all requests info by client_id

    :returns: a dict with the operation result

    """
    return Request.query.filter(Request.client_id == client_id).order_by(Request.client_priority).all()


def get_client_pending_requests(client_id):
    """
    Get all requests info by client_id

    :returns: a dict with the operation result

    """
    return Request.query.filter(Request.client_id == client_id, Request.attended).order_by(Request.client_priority).all()


def get_request_by_id(request_id=None):
    """
    Get request info by id

    :request_id: an integer object
    :returns: a request object
    """
    try:
        request = Request.query.get(request_id)
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    return request


def get_first_priority_client(client_id):
    request = Request.query.filter(Request.client_id == client_id, Request.attended == False)\
        .order_by(Request.client_priority).first()
    return request


def update_request(request_id, kwargs):
    """
    Creates a request.

    :request_id: an integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: request updated

    """
    try:
        request = Request.query.get(request_id)
        request.update(**kwargs)
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    except Exception as e:
        raise BaseIWSExceptions(arg=e.arg[0])
    return request


def insert_request_priority(request):
    """
    Creates a request.

    :request: an integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: request updated

    """
    try:
        next = None
        prev = Request.query.filter(Request.client == request.client, Request.attended == False,
            Request.client_priority < request.client_priority).order_by(- Request.client_priority).first()
        if not prev :
            next = Request.query.filter(Request.client == request.client, Request.attended == False,
                Request.client_priority >= request.client_priority).order_by(Request.client_priority).first()
            if not next:
                return
        if next:
            request.next = next
            request = request.save()
        elif prev:
            request.next = prev.next
            prev.next = request
            prev.save()
            request = request.save()
        update_priority_list(request)
    except Exception as e:
        raise BaseIWSExceptions(arg=e.args[0])
    return request


def update_priority_list(request):
    """
    Creates a request.

    :request: an integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: request updated

    """
    pivot = request
    while pivot.next:
        if pivot.client_priority == pivot.next.client_priority:
            pivot.next.client_priority += 1
            pivot = pivot.next.save()
        else:
            break


def update_request_on_priority_list(request):
    """
    Creates a request.

    :request: a integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: request updated

    """
    request = remove_request_from_priority_list(request)
    if request.attended:
        request = insert_request_priority(request)
    return request


def remove_request_from_priority_list(request):
    if request.next:
        if request.previous:
            prev = get_request_by_id(request.previous)
            prev.next = request.next
            prev.save()
        request.next = None
        request = request.save()
    return request


def delete_request(request_id):
    """
    Delete a request by id.

    :request_id: a int object
    :returns: boolean
    """
    try:
        request = Request.query.get(request_id)
        request = remove_request_from_priority_list(request)
        request.delete()
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    return True
