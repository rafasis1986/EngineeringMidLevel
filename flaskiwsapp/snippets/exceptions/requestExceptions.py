'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException


class RequestExistsException(LogicalException):

    def __init__(self, argument=None):
        super(RequestExistsException, self).__init__()
        self.message = 'The Request %s already exists' % argument


class RequestDoesnotExistsException(LogicalException):

    def __init__(self, argument=None):
        super(RequestDoesnotExistsException, self).__init__()
        self.message = 'The Request %s does not exists' % argument
