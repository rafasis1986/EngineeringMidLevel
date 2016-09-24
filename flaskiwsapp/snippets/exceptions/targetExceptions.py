'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException


class TargetExistsException(LogicalException):

    def __init__(self, argument=None):
        super(TargetExistsException, self).__init__()
        self.message = 'The Target %s already exists' % argument


class TargetDoesnotExistsException(LogicalException):

    def __init__(self, argument=None):
        super(TargetDoesnotExistsException, self).__init__()
        self.message = 'The Target %s does not exists' % argument
