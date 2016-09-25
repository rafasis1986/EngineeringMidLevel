'''
Created on Sep 16, 2016

@author: rtorres
'''
from marshmallow_jsonapi import Schema, fields
from inflection import dasherize
from flaskiwsapp.settings.baseConfig import BaseConfig


class BaseUserJsonSchema(Schema):
    """A Schema for many users model."""
    id = fields.Int()
    email = fields.Str()
    full_name = fields.Str()

    class Meta:
        type_ = 'user'
        strict = True
        inflect = dasherize
        self_url = '/api/%s/users/{id}' % BaseConfig.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/api/%s/users/' % BaseConfig.API_VERSION


class UserJsonSchema(BaseUserJsonSchema):
    """A Schema for user model."""
    first_name = fields.Str()
    last_name = fields.Str()
    created_at = fields.DateTime()
