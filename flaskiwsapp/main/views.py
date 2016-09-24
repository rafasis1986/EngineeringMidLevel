# -*- coding: utf-8 -*-
"""
Contains basic routes and helper functions
"""

from flask import Blueprint

from flaskiwsapp.extensions import login_manager
from flaskiwsapp.users.controllers.userControllers import get_user_by_id


main_blueprint = Blueprint('main', __name__, url_prefix='',
                           static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(int(user_id))
