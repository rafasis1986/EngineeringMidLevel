from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flaskiwsapp.snippets.exceptions.targetExceptions import TargetDoesnotExistsException, \
    TargetExistsException
from flaskiwsapp.projects.models.target import Target



def get_all_targets():
    """
    Get all targets info

    :returns: a dict with the operation result

    """
    # filter(Target.email.like('%rafa%')).all()
    return Target.query.all()


def get_target_by_id(target_id=None):
    """
    Get target info by id

    :target_id: a integer object
    :returns: a target object
    """
    try:
        target = Target.query.get(target_id)
    except NoResultFound:
        raise TargetDoesnotExistsException(target_id)
    return target


def update_target(target_id, kwargs):
    """
    Creates an target.

    :target_id: a integer object. Indicates an update.
    :kwargs: dictionary with the fields keys and values
    :returns: target updated

    """
    try:
        target = Target.query.get(target_id)
        target.update(**kwargs)
    except NoResultFound:
        raise TargetDoesnotExistsException(target_id)
    except Exception as e:
        raise BaseIWSExceptions(arg=e.arg[0])
    return target


def delete_target(target_id):
    """
    Delete an target by target id.

    :target_id: a int object
    :returns: boolean
    """
    try:
        Target.query.get(target_id).delete()
    except NoResultFound:
        raise TargetDoesnotExistsException(target_id)
    return True
