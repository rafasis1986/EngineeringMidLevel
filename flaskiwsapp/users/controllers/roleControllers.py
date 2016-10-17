'''
Created on Oct 14, 2016

@author: rtorres
'''
from sqlalchemy.orm.exc import NoResultFound
from flaskiwsapp.snippets.exceptions.roleExceptions import RoleDoesNotExistsException, RoleExistsException
from flaskiwsapp.users.models.role import Role
from sqlalchemy.exc import IntegrityError


def create_role(name):
    """
    Create a role info

    :name: a string object
    :returns: a role instance
    """
    try:
        role = Role(name=name)
        role.save()
    except IntegrityError:
        raise RoleExistsException(name)
    return role


def get_all_roles():
    """
    Get all clients info

    :returns: a dict with the operation result

    """
    # filter(Client.email.like('%rafa%')).all()
    return Role.query.all()


def get_role_by_id(role_id=None):
    """
    Get role info by id

    :role_id: a integer object
    :returns: a role object
    """
    try:
        role = Role.query.get(role_id)
    except NoResultFound:
        raise RoleDoesNotExistsException(role_id)
    return role


def get_role_by_name(role_name=None):
    """
    Get role info

    :role_name: a string object
    :returns: a role instance
    """
    try:
        role = Role.query.filter(Role.name == role_name).one()
    except NoResultFound:
        raise RoleDoesNotExistsException(role_name)
    return role
