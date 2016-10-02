'''
Created on Sep 24, 2016

@author: rtorres
'''
from flaskiwsapp.database import Model, SurrogatePK, db
from flaskiwsapp.users.customMixins import UserCustomMixion


class Client(UserCustomMixion, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'clients'

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
        """Return the id to satisfy Flask-Login's requirements"""
        return self.id
