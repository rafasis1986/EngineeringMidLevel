'''
Created on Sep 24, 2016

@author: rtorres
'''
from marshmallow_jsonapi import Schema, fields
from inflection import dasherize
from flaskiwsapp.settings.baseConfig import BaseConfig


class ClientJsonSchema(Schema):
    """A Schema for client model."""
    id = fields.Int()
    email = fields.Str()

    class Meta:
        type_ = 'client'
        strict = True
        inflect = dasherize
        self_url = '/api/%s/clients/{id}' % BaseConfig.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/api/%s/clients/' % BaseConfig.API_VERSION
