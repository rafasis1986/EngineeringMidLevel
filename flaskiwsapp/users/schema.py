'''
Created on Sep 16, 2016

@author: rtorres
'''
from flaskiwsapp.extensions import ma
from flaskiwsapp.users.models import Role, User
from marshmallow_jsonapi import Schema, fields
from inflection import dasherize
from flaskiwsapp import settings


class RoleSchema(ma.ModelSchema):
    """A schema for role model."""
    author = ma.HyperlinkRelated('user_detail')

    class Meta:
        model = Role


class UserSchema(ma.ModelSchema):
    """A Schema for user model."""

    class Meta:
        model = User
        fields = ('email', 'username')


class UserJsonSchema(Schema):
    """A Schema for user model."""
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()

    class Meta:
        type_ = 'user'
        strict = True
        inflect = dasherize
        self_url = '/api/%s/users/{id}' % settings.Config.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/api/%s/users/' % settings.Config.API_VERSION
