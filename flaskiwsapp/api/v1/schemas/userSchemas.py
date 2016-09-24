'''
Created on Sep 16, 2016

@author: rtorres
'''
from marshmallow_jsonapi import Schema, fields
from inflection import dasherize
from flaskiwsapp.settings.baseConfig import BaseConfig


class UserJsonSchema(Schema):
    """A Schema for user model."""
    id = fields.Int()
    email = fields.Str()

    class Meta:
        type_ = 'user'
        strict = True
        inflect = dasherize
        self_url = '/api/%s/users/{id}' % BaseConfig.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/api/%s/users/' % BaseConfig.API_VERSION
