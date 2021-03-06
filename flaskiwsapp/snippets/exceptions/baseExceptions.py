'''
Created on Sep 22, 2016

@author: rtorres
'''
from flask_api.status import HTTP_500_INTERNAL_SERVER_ERROR,\
    HTTP_503_SERVICE_UNAVAILABLE


class BaseIWSExceptions(Exception):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Base exception to iws be'

    def __init__(self, arg=None):
        if arg:
            self.message = arg


class TechnicalException(BaseException):

    def __init__(self):
        super(TechnicalException, self).__init__()
        self.message = 'Technical exception to iws be'


class LogicalException(BaseException):

    def __init__(self):
        super(LogicalException, self).__init__()
        self.message = 'Logical exception to iws be'
        self.status_code = HTTP_503_SERVICE_UNAVAILABLE
