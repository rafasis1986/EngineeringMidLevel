'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException


class RoleExistsException(LogicalException):

    def __init__(self, argument=None):
        super(RoleExistsException, self).__init__()
        self.message = 'The role %s already exists' % argument


class RoleDoesNotExistsException(LogicalException):

    def __init__(self, argument=None):
        super(RoleDoesNotExistsException, self).__init__()
        self.message = 'The role %s does not exists' % argument
