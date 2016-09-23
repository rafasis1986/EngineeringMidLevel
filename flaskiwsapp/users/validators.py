'''
Created on Sep 22, 2016

@author: rtorres
'''
from wtforms import validators
from flaskiwsapp.users.controllers import get_user_by_email
from flaskiwsapp.snippets.exceptions.userExceptions import UserDoesnotExistsException


def get_user(form):
    """Wrapper to get user info from a form  by the email of the form.data."""
    try:
        return (get_user_by_email(form.email.data))
    except UserDoesnotExistsException as e:
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
