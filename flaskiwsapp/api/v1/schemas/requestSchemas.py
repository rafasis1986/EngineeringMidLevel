'''
Created on Sep 24, 2016

@author: rtorres
'''
from inflection import underscore
from marshmallow_jsonapi import Schema, fields

from flaskiwsapp.settings.baseConfig import BaseConfig


class RequestJsonSchema(Schema):
    """A Schema for request model."""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    product_area = fields.Str()
    target_date = fields.DateTime()
    ticket_url = fields.Str()

    class Meta:
        type_ = 'request'
        strict = True
        inflect = underscore
        self_url = '/api/%s/requests/{id}' % BaseConfig.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/api/%s/requests/' % BaseConfig.API_VERSION
