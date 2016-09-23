# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from flaskiwsapp.database import db
from flaskiwsapp.users.models import User


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: 'user{0}'.format(n))
    username = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')
    active = True
    is_admin = False

    class Meta:
        """Factory configuration"""
        model = User
