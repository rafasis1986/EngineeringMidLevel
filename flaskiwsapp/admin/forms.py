# -*- coding: utf-8 -*-
"""Forms for user registration and login"""
from wtforms import PasswordField
from wtforms.validators import DataRequired, URL

from flaskiwsapp.users.forms import LoginForm
from flaskiwsapp.users.validators import validate_login, is_admin, is_phone
from flask_wtf.form import Form
from wtforms.fields.html5 import EmailField, TelField
from wtforms.fields import StringField
from wtforms_alchemy import ModelForm
from flaskiwsapp.projects.models.request import Request


class AdminLoginForm(LoginForm):
    """
    Admin login form. Only users with the 'is_admin' flag pass the form
    validation.
    """
    password = PasswordField('Password', validators=[DataRequired(),
                                                     validate_login,
                                                     is_admin])


class AdminClientForm(Form):
    email = EmailField('Email', validators=[DataRequired()])
    phone_number = TelField('Phone', validators=[DataRequired(), is_phone])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])


class AdminRequestForm(ModelForm):

    class Meta:
        model = Request
        exclude = ['attended', 'attended_date']


    ticket_url = StringField(validators=[DataRequired(), URL()])
