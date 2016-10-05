'''
Created on Sep 24, 2016

@author: rtorres
'''
from inflection import underscore
from flaskiwsapp.settings.baseConfig import BaseConfig
from flaskiwsapp.api.v1.schemas.userSchemas import BaseUserJsonSchema, UserDetailJsonSchema
from marshmallow_jsonapi.schema import Schema
from marshmallow_jsonapi import fields


class BaseClientJsonSchema(BaseUserJsonSchema):
    """A Simple Schema for client model."""

    class Meta:
        type_ = 'client'
        inflect = underscore
        self_url = '/api/%s/clients/{id}' % BaseConfig.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/api/%s/clients/' % BaseConfig.API_VERSION


class ClientDetailJsonSchema(UserDetailJsonSchema, BaseClientJsonSchema):
    """A Schema for client model."""
    pass


class ClientsEmailsJsonSchema(Schema):
    email = fields.Str()

    class Meta:
        type_ = 'client'
