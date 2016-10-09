'''
Created on Sep 22, 2016

@author: rtorres
'''
from wtforms import validators
from flaskiwsapp.users.controllers.userControllers import get_user_by_email
from flaskiwsapp.snippets.exceptions.userExceptions import UserDoesNotExistsException
from wtforms.validators import Regexp
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException


def get_user(form):
    """Wrapper to get user info from a form  by the email of the form.data."""
    try:
        return (get_user_by_email(form.email.data))
    except UserDoesNotExistsException as e:
        raise validators.ValidationError(e.message)


def validate_login(form, field):
    """Checks if a certain user exists, and if the forms hashed password
    matches the hash inside the database."""
    user = get_user(form)

    if user is None:
        raise validators.ValidationError('Invalid user or password')

    if not user.check_password(form.password.data):
        raise validators.ValidationError('Invalid user or password')


def is_admin(form, field):
    """
    Checks if a certain user is an admin and otherwise throws a
    validation error.
    """
    user = get_user(form)
    if not user.is_admin:
        raise validators.ValidationError('Invalid user or password')


def is_phone(form, field):
    """
    Checks if a string is a E.164 phonenumber
    """
    try:
        phonenumbers.parse(field.data, None)
    except NumberParseException as e:
        raise validators.ValidationError(e.args[0])
