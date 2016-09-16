'''
Created on Sep 16, 2016

@author: rtorres
'''
from flask_restful import Api
from flask_jwt import JWTError
from flask import jsonify
import collections
from flask_api.status import HTTP_500_INTERNAL_SERVER_ERROR


class CustomApi(Api):
    """A simple class to keep the default Errors behaviour."""

    def handle_error(self, e):
        if isinstance(e, JWTError):
            return jsonify(
                collections.OrderedDict([
                    ('status_code', e.status_code),
                    ('error', e.error),
                    ('description', e.description),
                ])
            ), e.status_code, e.headers
        elif isinstance(e, Exception):
            return jsonify(
                collections.OrderedDict([
                    ('status_code', HTTP_500_INTERNAL_SERVER_ERROR),
                    ('error', str(type(e))),
                    ('description', e.args[0]),
                ])
            ), HTTP_500_INTERNAL_SERVER_ERROR
        return super(CustomApi, self).handle_error(e)
