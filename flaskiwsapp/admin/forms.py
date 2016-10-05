# -*- coding: utf-8 -*-
"""Forms for user registration and login"""
from wtforms import PasswordField
from wtforms.validators import DataRequired

from flaskiwsapp.users.forms import LoginForm
from flaskiwsapp.users.validators import validate_login, is_admin


class AdminLoginForm(LoginForm):
    """
    Admin login form. Only users with the 'is_admin' flag pass the form
    validation.
    """
    password = PasswordField('Password', validators=[DataRequired(),
                                                     validate_login,
                                                     is_admin])
