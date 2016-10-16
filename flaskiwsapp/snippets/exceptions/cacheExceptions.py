'''
Created on Oct 16, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException
from flask_api.status import HTTP_405_METHOD_NOT_ALLOWED


class CacheExpiredException(LogicalException):

    def __init__(self, argument=None):
        super(CacheExpiredException, self).__init__()
        self.message = 'The key %s has expired' % argument
        self.status_code = HTTP_405_METHOD_NOT_ALLOWED
