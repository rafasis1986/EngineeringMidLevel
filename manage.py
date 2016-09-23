#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Management script."""
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell
from flask_script.commands import Clean, ShowUrls

from flaskiwsapp.app import create_app
from flaskiwsapp.database import db
from flaskiwsapp.users.models import User
from flaskiwsapp.snippets.helpers import register_token_auth
from flaskiwsapp.settings.prodConfig import ProdConfig
from flaskiwsapp.settings.devConfig import DevConfig
from flaskiwsapp.users.controllers import update_user, create_user
from flaskiwsapp.snippets.exceptions.userExceptions import UserExistsException


CONFIG = ProdConfig if os.environ.get('IWS_BE') == 'prod' else DevConfig
HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

app = create_app(CONFIG)
manager = Manager(app)
migrate = Migrate(app, db)
jwt = register_token_auth(app)


def _make_context():
    """Return context dict for a shell session so you can access app, db, and
    the User model by default."""
    return {'app': app, 'db': db, 'User': User}


@manager.command
def test():
    """run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


@manager.command
def create_admin():
    """Create a default admin user to get access to the admin panel."""
    try:
        user = create_user('admin@example.com', 'admin')
        update_user(user.id, {'is_admin': True, 'active': True})
    except UserExistsException:
        print('Admin user already exists. Try to login with: \n',
              'email: admin \n',
              'password: admin')

manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls())
manager.add_command('clean', Clean())

if __name__ == '__main__':
    manager.run()
