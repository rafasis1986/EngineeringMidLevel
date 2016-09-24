'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException


class UserExistsException(LogicalException):

    def __init__(self, argument=None):
        super(UserExistsException, self).__init__()
        self.message = 'The user %s already exists' % argument


class UserDoesnotExistsException(LogicalException):

    def __init__(self, argument=None):
        super(UserDoesnotExistsException, self).__init__()
        self.message = 'The user %s does not exists' % argument


class UserInactiveException(LogicalException):

    def __init__(self, argument=None):
        super(UserInactiveException, self).__init__()
        self.message = 'The user %s has benn inactive' % argument
