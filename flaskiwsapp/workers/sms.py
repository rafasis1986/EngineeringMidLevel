'''
Created on Oct 7, 2016

@author: rtorres
'''

from flask.globals import current_app
from twilio.rest.client import TwilioRestClient

from flaskiwsapp.extensions import celery
from flaskiwsapp.projects.controllers.requestControllers import get_request_by_id
from flaskiwsapp.projects.controllers.ticketControllers import get_ticket_by_id
from flaskiwsapp.snippets.logger import iws_logger, MSG_ERROR
from flaskiwsapp.users.controllers.clientControllers import get_client_by_id


@celery.task
def welcome_client_sms(client_id):
    try:
        client = get_client_by_id(client_id)
        twilio = TwilioRestClient(current_app.config['TWILIO_SID'], current_app.config['TWILIO_TOKEN'])
        message = twilio.messages.create(to=client.phone_number.e164, from_=current_app.config['TWILIO_PHONE'],
            body='%s welcome to %s' % (client.full_name, current_app.config['APP_NAME']))
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info('Twilio id: %s' % message.sid)


@celery.task
def create_request_sms(request_id):
    try:
        request = get_request_by_id(request_id)
        twilio = TwilioRestClient(current_app.config['TWILIO_SID'], current_app.config['TWILIO_TOKEN'])
        message = twilio.messages.create(to=request.client.phone_number.e164, from_=current_app.config['TWILIO_PHONE'],
            body='Created feature %s with priority %s and id %s' % (request.title, request.client_priority, request.id))
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info('Twilio id: %s' % message.sid)


@celery.task
def create_ticket_sms(ticket_id):
    try:
        ticket = get_ticket_by_id(ticket_id)
        created = "{:%d, %b %Y}".format(ticket.created_at)
        twilio = TwilioRestClient(current_app.config['TWILIO_SID'], current_app.config['TWILIO_TOKEN'])
        message = twilio.messages.create(to=ticket.request.client.phone_number.e164, from_=current_app.config['TWILIO_PHONE'],
            body='Feture %s attended with ticket %s , by %s the date %s' % (ticket.request.id, ticket.id, ticket.user.email, created))
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info('Twilio id: %s' % message.sid)
