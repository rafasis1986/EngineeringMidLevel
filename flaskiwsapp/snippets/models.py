'''
Created on Sep 14, 2016

@author: rtorres
'''
from sqlalchemy.orm import validates
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class EmailAddress(Base):
    __tablename__ = 'address'

    email = Column(String, primary_key=True)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address
