'''
Created on Oct 7, 2016

@author: rtorres
'''

from flask.globals import current_app
from sendgrid.helpers.mail import Mail, Content, Email
from sendgrid.sendgrid import SendGridAPIClient

from flaskiwsapp.extensions import celery
from flaskiwsapp.projects.controllers.ticketControllers import get_ticket_by_id
from flaskiwsapp.snippets.logger import iws_logger
from flaskiwsapp.users.controllers.userControllers import get_user_by_id
from flaskiwsapp.workers.constants import MSG_ERROR


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
    else:
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
    else:
        iws_logger.info('Send email status: %s' % response.status)



