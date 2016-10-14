'''
Created on Sep 16, 2016

@author: rtorres
'''
from marshmallow_jsonapi import Schema, fields
from inflection import underscore
from flaskiwsapp.settings.baseConfig import BaseConfig


class BaseUserJsonSchema(Schema):
    """A Simple Schema for many users model."""
    id = fields.Int()
    email = fields.Str()
    full_name = fields.Str()

    class Meta:
        type_ = 'user'
        strict = True
        inflect = underscore
        self_url = '/%s/users/{id}' % BaseConfig.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/%s/users/' % BaseConfig.API_VERSION


class UserDetailJsonSchema(BaseUserJsonSchema):
    """A Schema for user model."""
    first_name = fields.Str()
    last_name = fields.Str()
    created_at = fields.DateTime()
    roles = fields.Relationship(
        '/users/{role_id}/roles',
        related_url_kwargs={'role_id': '<id>'},
        # Include resource linkage
        many=True, include_resource_linkage=True,
        type_='role',
        id_field='name')
