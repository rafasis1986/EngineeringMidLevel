'''
Created on Sep 24, 2016

@author: rtorres
'''
from inflection import underscore
from marshmallow_jsonapi import Schema, fields

from flaskiwsapp.settings.baseConfig import BaseConfig

from flaskiwsapp.api.v1.schemas.userSchemas import BaseUserJsonSchema
from flaskiwsapp.api.v1.schemas.requestSchemas import BaseRequestJsonSchema


BASE_URL = '/api/%s/tickets/' % BaseConfig.API_VERSION
REQUEST_URL = '/api/%s/requests/{id}' % BaseConfig.API_VERSION
USER_URL = '/api/%s/users/{id}' % BaseConfig.API_VERSION


class BaseTicketJsonSchema(Schema):
    """A Simple Schema for ticket model."""
    id = fields.Integer()
    detail = fields.Str()
    created_at = fields.DateTime()
    request = fields.Relationship(
        related_url=REQUEST_URL,
        related_url_kwargs={'id': '<request.id>'},
        include_resource_linkage=True,
        type_='request',
        schema=BaseRequestJsonSchema)
    user = fields.Relationship(
        related_url=USER_URL,
        related_url_kwargs={'id': '<user.id>'},
        include_resource_linkage=True,
        type_='user',
        id_field='email',
        schema=BaseUserJsonSchema
    )

    class Meta:
        type_ = 'ticket'
        strict = True
        inflect = underscore
        self_url = BASE_URL + '{id}'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = BASE_URL
