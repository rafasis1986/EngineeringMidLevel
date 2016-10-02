'''
Created on Oct 1, 2016

@author: rtorres
'''
import datetime

from flaskiwsapp.database import SurrogatePK, Model, db, reference_col, relationship, Column


class Ticket(SurrogatePK, Model):
    """A ticket of the app."""

    __tablename__ = 'tickets'
    request_id = reference_col('requests', nullable=False, unique=True)
    request = relationship('Request', backref='ticket', uselist=False)
    user_id = reference_col('users', nullable=False)
    user = relationship('User', backref='ticket')
    detail = Column(db.Text(), nullable=False)
    created_at = Column(db.DateTime(), default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

    def __str__(self):
        """String representation of the tickets. Shows the id and id request."""
        return '%s - %s' % (self.id, self.request_id)

    def get_id(self):
        return self.id
