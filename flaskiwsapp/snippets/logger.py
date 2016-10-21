'''
Created on Oct 8, 2016

@author: rtorres
'''
import logging
import logging.config
import loggly.handlers

MSG_ERROR = 'Error %s, Message: %s'
MSG_TASK = 'Task: %s, id: %s'

logging.config.fileConfig('loggly.conf')

iws_logger = logging.getLogger('myLogger')
