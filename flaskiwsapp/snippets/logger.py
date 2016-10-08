'''
Created on Oct 8, 2016

@author: rtorres
'''
import logging
import logging.config
import loggly.handlers

logging.config.fileConfig('loggly.conf')

iws_logger = logging.getLogger('myLogger')
