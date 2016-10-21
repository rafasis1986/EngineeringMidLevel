'''
Created on Sep 23, 2016

@author: rtorres
'''
from flask_login import AnonymousUserMixin

from flaskiwsapp.database import Column, Model, SurrogatePK, db
from flaskiwsapp.settings.baseConfig import BaseConfig
from flaskiwsapp.users.customMixins import UserCustomMixion


class User(UserCustomMixion, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'users'
    admin = Column(db.Boolean(), default=False)
    social = Column(db.String(80), default=BaseConfig.APP_NAME)
    social_id = Column(db.String(80), default=BaseConfig.APP_NAME)
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email="", password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def __str__(self):
        """String representation of the user. Shows the users email address."""
        return self.email

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements"""
        return self.id

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    @property
    def is_admin(self):
        return self.admin
