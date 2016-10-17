'''
Created on Oct 14, 2016

@author: rtorres
'''
from flaskiwsapp.database import Column, db, SurrogatePK, Model
from sqlalchemy.sql.schema import ForeignKey


class Role(SurrogatePK, Model):

    name = Column(db.String(80), unique=True)

    def __str__(self):
        """String representation of the user. Shows the users email address."""
        return self.name


class UserRoles(SurrogatePK, Model):

    user_id = Column(db.Integer(), ForeignKey('users.id', ondelete='CASCADE'))
    role_id = Column(db.Integer(), ForeignKey('role.id', ondelete='CASCADE'))
