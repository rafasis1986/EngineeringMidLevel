'''
Created on Oct 7, 2016

@author: rtorres
'''
from flaskiwsapp.workers import sms, emails
from flaskiwsapp.snippets.logger import iws_logger


def create_welcome_client_job(client_id):
    try:
        task = sms.welcome_client_sms.delay(client_id)
    except Exception as e:
        iws_logger.error(type(e), e.args[0])
    else:
        iws_logger.info('status: %s, id: %s' % (task.status, task.id))


def create_request_sms_job(request_id):
    try:
        task = sms.create_request_sms(request_id)
    except Exception as e:
        iws_logger.error(type(e), e.args[0])
    else:
        iws_logger.info('status: %s, id: %s' % (task.status, task.id))


def create_ticket_sms_job(ticket_id):
    try:
        task = sms.create_ticket_sms(ticket_id)
    except Exception as e:
        iws_logger.error(type(e), e.args[0])
    else:
        iws_logger.info('status: %s, id: %s' % (task.status, task.id))


def create_welcome_email_job(user_id):
    try:
        task = emails.welcome_user_email(user_id)
    except Exception as e:
        iws_logger.error(type(e), e.args[0])
    else:
        iws_logger.info('status: %s, id: %s' % (task.status, task.id))


def create_ticket_email_job(ticket_id):
    try:
        task = emails.ticket_created_email(ticket_id)
    except Exception as e:
        iws_logger.error(type(e), e.args[0])
    else:
        iws_logger.info('status: %s, id: %s' % (task.status, task.id))
