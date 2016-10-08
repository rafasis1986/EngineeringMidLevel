'''
Created on Oct 7, 2016

@author: rtorres
'''
from flaskiwsapp.workers import sms, emails
from flaskiwsapp.snippets.logger import iws_logger
from flaskiwsapp.workers.constants import MSG_ERROR, MSG_TASK


def create_welcome_client_job(client_id):
    try:
        task = sms.welcome_client_sms.delay(client_id)
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info(MSG_TASK % (task.task_name, task.id))


def create_request_sms_job(request_id):
    try:
        task = sms.create_request_sms.delay(request_id)
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info(MSG_TASK % (task.task_name, task.id))


def create_ticket_sms_job(ticket_id):
    try:
        task = sms.create_ticket_sms.delay(ticket_id)
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info(MSG_TASK % (task.task_name, task.id))


def create_welcome_user_email_job(user_id):
    try:
        task = emails.welcome_user_email.delay(user_id)
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info(MSG_TASK % (task.task_name, task.id))


def create_ticket_email_job(ticket_id):
    try:
        task = emails.ticket_created_email.delay(ticket_id)
    except Exception as e:
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
    else:
        iws_logger.info(MSG_TASK % (task.task_name, task.id))
