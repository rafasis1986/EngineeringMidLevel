'''
Created on Sep 24, 2016

@author: rtorres
'''
import datetime

from flask_login import UserMixin
from flaskiwsapp.database import Column, db


class UserCustomMixion(UserMixin):
    """A user mixin of the app."""

    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.Binary(60), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    first_name = Column(db.String(80), nullable=True)
    last_name = Column(db.String(80), nullable=True)
    active = Column(db.Boolean(), default=False)
