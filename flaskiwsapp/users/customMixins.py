'''
Created on Sep 24, 2016

@author: rtorres
'''
import datetime

from flask_login import UserMixin

from flaskiwsapp.database import Column, db
from flaskiwsapp.extensions import bcrypt
from sqlalchemy_utils.types.phone_number import PhoneNumberType


class UserCustomMixion(UserMixin):
    """A user mixin of the app."""

    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.Binary(60), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    first_name = Column(db.String(80), nullable=True)
    last_name = Column(db.String(80), nullable=True)
    active = Column(db.Boolean(), default=False)
    phone_number = Column(PhoneNumberType(), unique=True)

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

    def has_role(self, *specified_role_names):
        """
        Return True if the user has one of the specified roles. Return False otherwise.
        """
        if hasattr(self, 'roles'):
            roles = self.roles
        else:
            if hasattr(self, 'user_profile') and hasattr(self.user_profile, 'roles'):
                roles = self.user_profile.roles
            else:
                roles = None
        if not roles:
            return False
        user_role_names = [role.name for role in roles]
        for role_name in specified_role_names:
            if role_name in user_role_names:
                return True
        return False
