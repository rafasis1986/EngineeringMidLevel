'''
Created on Oct 7, 2016

@author: rtorres
'''

from flaskiwsapp.extensions import celery
from flaskiwsapp.snippets.logger import iws_logger
from flask.globals import current_app
from flaskiwsapp.users.controllers.userControllers import get_user_by_id
from sendgrid.sendgrid import SendGridAPIClient
from sendgrid.helpers.mail.mail import Mail, Content
from flaskiwsapp.projects.controllers.ticketControllers import get_ticket_by_id


@celery.task
def welcome_user_email(user_id):
    try:
        from_email = current_app.config['SENDGRID_EMAIL']
        token = current_app.config['SENDGRID_TOKEN']
        subject = "Welcome [IWS]"
        user = get_user_by_id(user_id)
        content = Content("text/plain", "Hello, from IWS")
        sg = SendGridAPIClient(apikey=token)
        mail = Mail(from_email, subject, user.email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
    except Exception as e:
        iws_logger.error(type(e), e.args[0])
    else:
        iws_logger.info('Send email status: %s' % response.status)


@celery.task
def ticket_created_email(ticket_id):
    try:
        from_email = current_app.config['SENDGRID_EMAIL']
        token = current_app.config['SENDGRID_TOKEN']
        subject = "Created Ticket [IWS]"
        ticket = get_ticket_by_id(ticket_id)
        content = Content("text/plain", "Your create the ticket %s with the detail: %s" % (ticket.id, ticket.detail))
        sg = SendGridAPIClient(apikey=token)
        mail = Mail(from_email, subject, ticket.user.email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
    except Exception as e:
        iws_logger.error(type(e), e.args[0])
    else:
        iws_logger.info('Send email status: %s' % response.status)
