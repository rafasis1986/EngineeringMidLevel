# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime
import pytest

from flaskiwsapp.main.views import load_user

from .factories import UserFactory
from flaskiwsapp.users.controllers.userControllers import get_user_by_id, create_user


@pytest.mark.usefixtures('db')
class TestUser:
    """User tests."""

    def test_get_by_id(self):
        """Get user by ID."""
        user = create_user('foo@bar.com')

        retrieved = get_user_by_id(user.id)
        assert retrieved == user

    def test_created_at_defaults_to_datetime(self):
        """Test creation date."""
        user = create_user(email='foo@bar.com')
        assert bool(user.created_at)
        assert isinstance(user.created_at, datetime.datetime)

    def test_password_is_nullable(self):
        """Test null password."""
        user = create_user(email='foo@bar.com')
        assert user.password is None

    def test_factory(self, db):
        """Test user factory."""
        user = UserFactory(password='myprecious')
        db.session.commit()
        assert bool(user.email)
        assert bool(user.created_at)
        assert user.is_admin is False
        assert user.active is True
        assert user.check_password('myprecious')

    def test_check_password(self):
        """Test check password."""
        user = create_user(email='foo@bar.com', password='foobarbaz123')
        assert user.check_password('foobarbaz123') is True
        assert user.check_password('lajfd') is False

    def test_full_name(self):
        """User full name."""
        user = UserFactory(first_name='Foo', last_name='Bar')
        assert user.full_name == 'Foo Bar'

    def test_string_representation(self):
        """Test string representation."""
        user = UserFactory(email="test@test.de")
        user.save()
        assert str(user) == 'test@test.de'

    def test_is_active(self):
        """Tests is_active method."""
        user = UserFactory(active=True)
        user.save()
        assert user.is_active

    def test_is_anonymous(self):
        """Test is_anonymous method."""
        user = UserFactory()
        user.save()
        assert user.is_anonymous is False

    def test_is_authenticated_is_true(self):
        """Test is_authenticated method."""
        user = UserFactory()
        user.save()
        assert user.is_authenticated is True


@pytest.mark.usefixtures('db')
def test_load_user():
    """Test load_user function."""
    user = create_user(email="ttester@test.com")
    assert user == load_user(user.get_id())
