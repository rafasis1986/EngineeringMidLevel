'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException


class UserExistsException(LogicalException):

    def __init__(self, argument=None):
        super(UserExistsException, self).__init__()
        self.message = 'The user {!r} already exists'.format(argument)


class UserDoesnotExistsException(LogicalException):

    def __init__(self, argument=None):
        super(UserExistsException, self).__init__()
        self.message = 'The user {!r} does not exists'.format(argument)
