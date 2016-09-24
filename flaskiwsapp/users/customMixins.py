'''
Created on Sep 24, 2016

@author: rtorres
'''
import datetime

from flask_login import UserMixin

from flaskiwsapp.database import Column, db
from flaskiwsapp.extensions import bcrypt


class UserCustomMixion(UserMixin):
    """A user mixin of the app."""

    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.Binary(60), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    first_name = Column(db.String(80), nullable=True)
    last_name = Column(db.String(80), nullable=True)
    active = Column(db.Boolean(), default=False)

    def set_password(self, password):
        """Set password"""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return "{0} {1}".format(self.first_name, self.last_name)

    @property
    def is_active(self):
        """Active or non active user (required by flask-login)"""
        return self.active
