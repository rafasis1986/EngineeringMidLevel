from flaskiwsapp.users.models import User


def get_users(username=None):
    """Get all users info. Accepts specify an username.

    :username: a string object
    :returns: a dict with the operation result

    """
    query = {} if not username else {'username': username}
    users = User.query.all()

    return users
