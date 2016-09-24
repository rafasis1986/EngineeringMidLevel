'''
Created on Sep 24, 2016

@author: rtorres
'''
from flaskiwsapp.database import SurrogatePK, Model, db, reference_col, relationship, Column
from sqlalchemy.dialects.postgresql.base import ENUM


AREAS = ('Policies', 'Billing', 'Claims', 'Reports')


class Target(SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'targets'
    title = Column(db.String(80), nullable=False)
    description = Column(db.Text(), nullable=False)
    client_id = reference_col('clients', nullable=True)
    client = relationship('Client', backref='targets')
    client_priority = Column(db.SmallInteger(), nullable=False)
    product_area = Column(ENUM(*AREAS, name='areas', create_type=False))

    def __init__(self, title="", password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, title=title.strip(), **kwargs)

    def __str__(self):
        """String representation of the user. Shows the target title."""
        return self.title

    def get_id(self):
        return self.id
