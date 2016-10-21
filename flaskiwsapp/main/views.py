# -*- coding: utf-8 -*-
"""
Contains basic routes and helper functions
"""

from flask import Blueprint

from flaskiwsapp.extensions import login_manager
from flaskiwsapp.users.controllers.userControllers import get_user_by_id
from werkzeug.utils import redirect
from flask.globals import current_app


main_blueprint = Blueprint('main', __name__, url_prefix='',
                           static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(int(user_id))


@main_blueprint.route('/', endpoint='login')
def index():
    """Renders the main page page."""
    return redirect(current_app.config['APP_URL'], code=302)
