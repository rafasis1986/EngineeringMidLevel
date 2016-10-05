'''
Created on Sep 24, 2016

@author: rtorres
'''
import datetime

from sqlalchemy.dialects.postgresql.base import ENUM

from flaskiwsapp.database import SurrogatePK, Model, db, reference_col, relationship, Column
from flaskiwsapp.projects.snippets.constants import AREAS


class Request(SurrogatePK, Model):
    """A request of the app."""

    __tablename__ = 'requests'
    title = Column(db.String(80), nullable=False)
    description = Column(db.Text(), nullable=False)
    client_id = reference_col('clients', nullable=False)
    client = relationship('Client', backref='request')
    client_priority = Column(db.SmallInteger(), nullable=False)
    created_at = Column(db.DateTime(), default=datetime.datetime.utcnow)
    product_area = Column(ENUM(*AREAS, name='areas', create_type=False), nullable=False)
    target_date = Column(db.Date(), nullable=False)
    ticket_url = Column(db.String(256), nullable=False)
    attended = Column(db.Boolean(), default=False)
    attended_date = Column(db.DateTime(), nullable=True)
    previous = reference_col('requests', nullable=True)
    next = relationship('Request', uselist=False)

    def __init__(self, title="", **kwargs):
        """Create instance."""
        db.Model.__init__(self, title=title.strip(), **kwargs)

    def __str__(self):
        """String representation of the request. Shows the title."""
        return self.title

    def get_id(self):
        return self.id

    def set_ticket_url(self, ticket_url):
        """Set ticket Url"""
        self.ticket_url = ticket_url

    def set_client_priority(self, priority):
        """Set client priority"""
        self.client_priority = priority
