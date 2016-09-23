'''
Created on Sep 22, 2016

@author: rtorres
'''
from flask_api.status import HTTP_500_INTERNAL_SERVER_ERROR


class AuthBaseException(Exception):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Base exception to auth'


class AuthSignUpException(AuthBaseException):

    def __init__(self, argument=None):
        super(AuthSignUpException, self).__init__()
        self.message = argument if argument else self.message


class AuthUpdateException(Exception):

    def __init__(self, argument=None):
        super(AuthUpdateException, self).__init__()
        self.message = argument if argument else self.message
