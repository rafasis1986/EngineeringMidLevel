'''
Created on Sep 22, 2016

@author: rtorres
'''
from flaskiwsapp.snippets.exceptions.userExceptions import UserExistsException
from flaskiwsapp.users.controllers import create_user, update_user
from manage import manager, TEST_PATH


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
              'username: admin \n',
              'password: admin')
