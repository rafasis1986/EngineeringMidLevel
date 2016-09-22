# -*- coding: utf-8 -*-
"""
Contains basic routes and helper functions
"""

from flask import Blueprint

from flaskiwsapp.extensions import login_manager
from flaskiwsapp.users.models import User


main_blueprint = Blueprint('main', __name__, url_prefix='',
                           static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))
