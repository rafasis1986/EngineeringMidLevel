# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""


from flask import Flask, render_template
from flask_admin import Admin

from flaskiwsapp.admin.views import MyAdminIndexView, UserView, RequestView, TicketView, MyModelView
from flaskiwsapp.api.v1.views.clientViews import clients_api_blueprint
from flaskiwsapp.api.v1.views.requestViews import requests_api_blueprint
from flaskiwsapp.api.v1.views.ticketViews import tickets_api_blueprint
from flaskiwsapp.api.v1.views.userViews import users_api_blueprint
from flaskiwsapp.api.v1.views.utilsViews import utils_api_blueprint
from flaskiwsapp.auth.views import auth_blueprint
from flaskiwsapp.extensions import bcrypt, db, migrate, login_manager, ma, celery, cache
from flaskiwsapp.main.views import main_blueprint
from flaskiwsapp.projects.models.request import Request
from flaskiwsapp.projects.models.ticket import Ticket
from flaskiwsapp.settings.baseConfig import BaseConfig
from flaskiwsapp.users.models.role import Role
from flaskiwsapp.users.models.user import User


def create_app(config_object=BaseConfig, blueprints=True):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories.

    :param config_object: The configuration object to use.
    """

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    if blueprints:
        register_blueprints(app)
    init_admin(app)
    init_celery(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cache.init_app(app, config={'CACHE_TYPE': app.config['CACHE_TYPE'],
                                'CACHE_DEFAULT_TIMEOUT': app.config['CACHE_DEFAULT_TIMEOUT']})
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    url_api = '/api/%s/{api}/' % app.config['API_VERSION']
    app.register_blueprint(main_blueprint)
    app.register_blueprint(users_api_blueprint, url_prefix=url_api.format(api='users'))
    app.register_blueprint(clients_api_blueprint, url_prefix=url_api.format(api='clients'))
    app.register_blueprint(requests_api_blueprint, url_prefix=url_api.format(api='requests'))
    app.register_blueprint(tickets_api_blueprint, url_prefix=url_api.format(api='tickets'))
    app.register_blueprint(auth_blueprint, url_prefix='/auth/')
    app.register_blueprint(utils_api_blueprint, url_prefix='/utils/')
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    for errcode in [401, 404, 500]:
        app.register_error_handler(errcode, render_error)

    return None


def init_admin(app):
    """Adds ModelViews to flask-admin."""
    admin = Admin(
        app,
        name="IWS-Admin",
        index_view=MyAdminIndexView(),
        base_template='my_master.html',
        endpoint="admin"
    )
    admin.add_view(UserView(User, db.session))
    admin.add_view(RequestView(Request, db.session))
    admin.add_view(TicketView(Ticket, db.session))
    admin.add_view(MyModelView(Role, db.session))
    return None


def init_celery(app):
    celery.conf.update(app.config)


####################
# Helper functions #
####################

def render_error(error):
    """Render error template"""
    # If a HTTPException, pull the `code` attribute; default to 500
    error_code = getattr(error, 'code', 500)

    error_code = parse_401_to_404(error_code)

    return render_template('{0}.html'.format(error_code)), error_code


def parse_401_to_404(error_code):
    """Parses a 401 error code to a 404."""

    # The user does not need to know that he is not
    # allowed to access a certain
    # resource. For security reasons the user should see the standard
    # 404 instead of an unauthorized error
    if error_code == 401:
        error_code = 404

    return error_code
