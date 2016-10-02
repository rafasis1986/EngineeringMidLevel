# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from flaskiwsapp.database import db
from flaskiwsapp.users.models.user import User
from flaskiwsapp.users.models.client import Client
import factory
from flaskiwsapp.projects.models.request import Request
import datetime
from flaskiwsapp.projects.snippets.constants import AREAS


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')
    active = True
    admin = False

    class Meta:
        """Factory configuration"""
        model = User


class AdminFactory(UserFactory):
    """Admin factory."""
    admin = True


class ClientFactory(BaseFactory):
    """Client factory."""

    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')
    active = True

    class Meta:
        """Factory configuration"""
        model = Client


class RequestFactory(BaseFactory):
    """Request factory."""
    title = Sequence(lambda n: 'title example {0}'.format(n))
    description = Sequence(lambda n: 'description {0}'.format(n))
    client = factory.SubFactory(ClientFactory)

    class Meta:
        """Factory configuration"""
        model = Request
