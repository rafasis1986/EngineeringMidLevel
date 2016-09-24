'''
Created on Sep 24, 2016

@author: rtorres
'''
from marshmallow_jsonapi import Schema, fields
from inflection import dasherize
from flaskiwsapp.settings.baseConfig import BaseConfig


class TargetJsonSchema(Schema):
    """A Schema for target model."""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    product_area = fields.Str()
    target_date = fields.DateTime()
    ticket_url = fields.Str()

    class Meta:
        type_ = 'target'
        strict = True
        inflect = dasherize
        self_url = '/api/%s/targets/{id}' % BaseConfig.API_VERSION
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/api/%s/targets/' % BaseConfig.API_VERSION
