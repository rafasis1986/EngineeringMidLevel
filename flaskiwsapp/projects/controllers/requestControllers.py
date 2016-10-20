from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.projects.models.request import Request
from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flaskiwsapp.snippets.exceptions.requestExceptions import RequestDoesnotExistsException
import datetime


def create_request(kwargs):
    request = Request(kwargs['title'])
    request = request.update(**kwargs)
    request = insert_request_priority(request)
    return request


def get_all_requests():
    """
    Get all requests info

    :returns: a dict with the operation result

    """
    return Request.query.order_by(Request.id).all()


def get_all_requests_attended(status=False):
    """
    Get all requests grouped by status

    :returns: a dict with the operation result

    """
    return Request.query.filter(Request.attended == status).order_by(Request.id).all()


def get_all_client_requests(client_id):
    """
    Get all requests info by client_id

    :returns: a dict with the operation result

    """
    return Request.query.filter(Request.client_id == client_id).order_by(Request.client_priority).all()


def get_client_pending_requests(client_id):
    """
    Get all pending requests info by client_id

    :returns: a dict with the operation result

    """
    return Request.query.filter(Request.client_id == client_id, Request.attended == False).order_by(Request.client_priority).all()


def get_requests_by_ids(requests_id, client_id):
    """
    Get a list of requests from a client

    :requests_id: a list of int with reqursts id
    :client_id: a int with client id info
    :returns: a dict with the operation result
    """
    return Request.query.filter(Request.client_id == client_id, Request.id.in_(requests_id)).all()


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
    request = Request.query.filter(Request.client_id == client_id, Request.attended==False)\
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
        legacy_priority = request.client_priority
        request.update(**kwargs)
        if (request.client_priority != legacy_priority):
            request = update_request_on_priority_list(request)
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    except Exception as e:
        raise BaseIWSExceptions(arg=e.arg[0])
    return request


def update_checked_request(request_id):
    """
    Checked a request.

    :request_id: an integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: request updated

    """
    try:
        request = Request.query.get(request_id)
        request.attended = True
        request.attended_date = datetime.datetime.utcnow()
        request.save()
        request = remove_request_from_priority_list(request)
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
        if not prev:
            next = Request.query.filter(Request.client == request.client, Request.attended == False,
                Request.client_priority >= request.client_priority, Request.id != request.id).order_by(Request.client_priority).first()
            if not next:
                return request
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
    if not request.attended:
        request = insert_request_priority(request)
    return request


def update_client_priority_list(requests_id, client_id):
    """
    Update the client priority_list for a client

    :requests_i: a list with integer objects.
    :client_id: a integer with client_id

    :returns: request updated
    """
    delete_request_priority_list(client_id)
    requests = get_requests_by_ids(requests_id, client_id)
    requests = sorted(requests, key=lambda request: requests_id.index(request.id))
    total_requests = len(requests)
    try:
        for iter in range(total_requests):
            requests[iter].client_priority = iter + 1
            if iter < (total_requests - 1):
                requests[iter].next = requests[iter + 1]
            requests[iter] = requests[iter].save()
    except Exception as e:
        print(e)
    return requests


def remove_request_from_priority_list(request):
    if request.previous:
        prev = get_request_by_id(request.previous)
        prev.next = request.next
        request.previous = None
        request.next = None
        request.save()
        prev.save()
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


def delete_me_request(request_id, client_id):
    """
    Delete a request for a client by id.

    :request_id: a int object
    :client_id: a int object
    :returns: boolean
    """
    try:
        request = Request.query.filter(Request.client_id == client_id, Request.id == request_id)
        request = remove_request_from_priority_list(request)
        request.delete()
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    return True


def delete_request_priority_list(client_id):
    """
    Delete a priority_list to client id.

    :client_id: a int
    :returns: boolean
    """
    requests = get_client_pending_requests(client_id)
    for item in requests:
        item.update(next=None)
    return True
