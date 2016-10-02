'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException


class ClientExistsException(LogicalException):

    def __init__(self, argument=None):
        super(ClientExistsException, self).__init__()
        self.message = 'The Client %s already exists' % argument


class ClientDoesnotExistsException(LogicalException):

    def __init__(self, argument=None):
        super(ClientDoesnotExistsException, self).__init__()
        self.message = 'The Client %s does not exists' % argument


class ClientInactiveException(LogicalException):

    def __init__(self, argument=None):
        super(ClientInactiveException, self).__init__()
        self.message = 'The Client %s has benn inactive' % argument
