'''
Created on Oct 7, 2016

@author: rtorres
'''

from flask.globals import current_app
from sendgrid.helpers.mail import Mail, Content, Email
from sendgrid.sendgrid import SendGridAPIClient

from flaskiwsapp.extensions import celery
from flaskiwsapp.projects.controllers.ticketControllers import get_ticket_by_id
from flaskiwsapp.snippets.logger import iws_logger, MSG_ERROR
from flaskiwsapp.users.controllers.userControllers import get_user_by_id
from flaskiwsapp.users.controllers.clientControllers import get_client_by_id
from flaskiwsapp.snippets.exceptions.clientExceptions import ClientDoesnotExistsException


@celery.task
def ticket_created_email(ticket_id):
    try:
        token = current_app.config['SENDGRID_TOKEN']
        subject = "Created Ticket [IWS]"
        ticket = get_ticket_by_id(ticket_id)
        from_email = Email(current_app.config['SENDGRID_EMAIL'])
        to_email = Email(ticket.user.email)
        content = Content("text/plain", "Your create the ticket %s with the detail: %s" % (ticket.id, ticket.detail))
        sg = SendGridAPIClient(apikey=token)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    if response and response.status:
        iws_logger.info('Send email status: %s' % response.status)


@celery.task
def welcome_user_email(user_id):
    try:
        token = current_app.config['SENDGRID_TOKEN']
        subject = "Welcome [IWS]"
        user = get_user_by_id(user_id)
        from_email = Email(current_app.config['SENDGRID_EMAIL'])
        to_email = Email(user.email)
        content = Content("text/plain", "Hello, from IWS")
        sg = SendGridAPIClient(apikey=token)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    if response and response.status:
        iws_logger.info('Send email status: %s' % response.status)


@celery.task
def create_confirm_email(client_id, key):
    try:
        token = current_app.config['SENDGRID_TOKEN']
        subject = "Confirmation code [IWS]"
        client = get_client_by_id(client_id)
        from_email = Email(current_app.config['SENDGRID_EMAIL'])
        to_email = Email(client.email)
        content = Content("text/plain", 'Confirmation message sent from IWS-Test, your code is: %s' % key)
        sg = SendGridAPIClient(apikey=token)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
    except ClientDoesnotExistsException as e:
        iws_logger.error(MSG_ERROR % (type(e), e.message))
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    if response and response.status:
        iws_logger.info('Send email status: %s' % response.status)
