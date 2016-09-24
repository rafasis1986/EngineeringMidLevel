# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from flaskiwsapp.app import create_app
from flaskiwsapp.database import db as _db


from .factories import UserFactory
from flaskiwsapp.settings.testConfig import TestConfig


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
    user = UserFactory(email="testuser@example.com", password='myprecious')
    db.session.commit()
    return user


@pytest.fixture
def admin(db):
    """A admin for the tests."""
    admin = UserFactory(email="admin@example.com", password="admin", admin=True)
    db.session.commit()
    return admin
