# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from flaskiwsapp.app import create_app
from flaskiwsapp.database import db as _db
from flaskiwsapp.extensions import bcrypt
from flaskiwsapp.settings import TestConfig
from flaskiwsapp.snippets.mails import make_ramdom_email
from flaskiwsapp.users.models import User

from .factories import UserFactory


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """A flask test client."""
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)


@pytest.yield_fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """A user for the tests."""
    user = UserFactory(username="testuser", password='myprecious')
    db.session.commit()
    return user


@pytest.fixture
def admin(db):
    """A admin for the tests."""
    admin = UserFactory(username="admin", password="admin", is_admin=True)
    db.session.commit()
    return admin
