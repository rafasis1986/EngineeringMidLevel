# -*- coding: utf-8 -*-
"""Forms for user registration and login"""
from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flaskiwsapp.users.validators import validate_login


class LoginForm(Form):
    """Basic login form."""
    email = StringField('Email', validators=[DataRequired(), Email(),
                                             Length(min=6, max=80)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6, max=50),
                                                     validate_login])


class RegisterForm(LoginForm):
    """Register form."""
    confirm = PasswordField('Verify Password',
                            validators=[DataRequired(),
                                        EqualTo('password',
                                        message='Passwords must match')])
