# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from flaskiwsapp.database import db
from flaskiwsapp.users.models.user import User
from flaskiwsapp.users.models.client import Client


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
