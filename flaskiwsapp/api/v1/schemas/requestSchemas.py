'''
Created on Sep 24, 2016

@author: rtorres
'''
from inflection import underscore
from marshmallow_jsonapi import Schema, fields

from flaskiwsapp.settings.baseConfig import BaseConfig
from flaskiwsapp.api.v1.schemas.clientSchemas import BaseClientJsonSchema

CLIENT_URL = '/api/%s/clients/{id}' % BaseConfig.API_VERSION
BASE_URL = '/api/%s/requests/' % BaseConfig.API_VERSION


class BaseRequestJsonSchema(Schema):
    """A Base Schema for request model."""
    id = fields.Int()
    title = fields.Str()
    product_area = fields.Str()
    target_date = fields.Time()
    attended = fields.Boolean()
    client_priority = fields.Int()
    client = fields.Relationship(
        related_url=CLIENT_URL,
        related_url_kwargs={'id': '<client.id>'},
        include_resource_linkage=True,
        type_='client',
        id_field='email',
        schema=BaseClientJsonSchema
    )

    class Meta:
        type_ = 'request'
        strict = True
        inflect = underscore
        self_url = BASE_URL + '{id}'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = BASE_URL


class RequestDetailJsonSchema(BaseRequestJsonSchema):
    """A Schema for detailed request ."""
    description = fields.Str()
    product_area = fields.Str()
    ticket_url = fields.Str()
    created_at = fields.DateTime()
    attended_date = fields.DateTime()
