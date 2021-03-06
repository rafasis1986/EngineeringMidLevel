from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.projects.controllers.requestControllers import update_checked_request
from flaskiwsapp.projects.models.ticket import Ticket
from flaskiwsapp.snippets.exceptions.requestExceptions import RequestDoesnotExistsException
from flaskiwsapp.projects.models.request import Request


def get_all_tickets():
    """
    Get all Tickects info

    :returns: a dict with the operation result

    """
    return Ticket.query.order_by(Ticket.id).all()


def get_tickets_user(user_id):
    """
    Get all tickets info by user_id

    :returns: a dict with the operation result

    """
    return Ticket.query.filter(Ticket.user_id == user_id).order_by(Ticket.id).all()


def get_tickets_by_client(client_id):
    """
    Get all the tickets to specific client

    :client_id: a integer object
    :returns: an ticket object
    """
    ticket = Ticket.query.join(Request).filter(Request.client_id == client_id).order_by(Ticket.id).all()
    return ticket


def get_ticket_by_id(ticket_id):
    """
    Get ticket info by id

    :ticket_id: a integer object
    :returns: a ticket object
    """
    try:
        ticket = Ticket.query.get(ticket_id)
    except NoResultFound:
        raise RequestDoesnotExistsException(ticket_id)
    return ticket


def get_ticket_by_request(request_id):
    """
    Get ticket info by request id

    :request_id: a integer object
    :returns: an ticket object
    """
    try:
        ticket = Ticket.query.filter(Ticket.request_id == request_id).first()
    except NoResultFound:
        raise RequestDoesnotExistsException(request_id)
    return ticket


def create_ticket(request, user, detail):
    """
    Create a ticket.

    :request: a request object.
    :user: an user object.
    :detail: a string object.
    :returns: ticket created

    """
    ticket = Ticket()
    ticket.user = user
    ticket.request = request
    ticket.detail = detail
    ticket = ticket.save()
    request = update_checked_request(request.id)
    return ticket


def delete_ticket(ticket_id):
    """
    Delete a ticket by id.

    :ticket_id: an int object
    :returns: ticket
    """
    try:
        ticket = Ticket.query.get(ticket_id)
        ticket.delete()
    except NoResultFound:
        raise RequestDoesnotExistsException(ticket_id)
    return True
