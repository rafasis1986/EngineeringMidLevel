'''
Created on Sep 16, 2016

@author: rtorres
'''
from flask_restful import Api
from flask_jwt import JWTError
from flask import jsonify
import collections
from flask_api.status import HTTP_501_NOT_IMPLEMENTED

DUMMY_ERROR_CODE = '1000'


class CustomApi(Api):
    """A simple class to keep the default Errors behaviour."""

    def handle_error(self, e):
        response_dict = {'data': {}}
        error = {}
        if isinstance(e, JWTError):
            error.update({'status': e.status_code})
            error.update({'title': e.error})
            error.update({'detail': e.description})
            error.update({'code': DUMMY_ERROR_CODE})
            response_dict['data'] = error
            return jsonify(response_dict), e.status_code, e.headers
        elif isinstance(e, Exception):
            error.update({'status': HTTP_501_NOT_IMPLEMENTED})
            error.update({'title': str(type(e))})
            error.update({'detail': e.args[0]})
            error.update({'code': DUMMY_ERROR_CODE})
            response_dict['data'] = error
            return jsonify(response_dict), HTTP_501_NOT_IMPLEMENTED, None
        return super(CustomApi, self).handle_error(e)
