from flask.blueprints import Blueprint
from flask_restful import Resource, reqparse
from flaskiwsapp.users.controllers import get_all_users, update_user, delete_user
from flask_jwt import jwt_required
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.users.schema import UserJsonSchema


def post_put_parser():
    """
    Request parser for HTTP POST or PUT.

    :returns: flask.ext.restful.reqparse.RequestParser object
    """
    parse = reqparse.RequestParser()
    parse.add_argument('email', type=str, location='json', required=True)
    parse.add_argument('password', type=str, location='json', required=True)

    return parse


class UsersAPI(Resource):
    """An API to get or create users."""

    @jwt_required()
    def get(self, email=None):
        """HTTP GET. Get one or all users.

        :email: a string valid as object id.
        :returns: One or all available users.

        """

        users = get_all_users()
        user_schema = UserJsonSchema(many=True)

        return user_schema.dump(users).data


class UserAPI(Resource):
    """An API to update or delete an user. """

    @jwt_required()
    def put(self, user_id):
        """
        HTTP PUT. Update an user.
        :returns:
        """

        parse = post_put_parser()
        parse.add_argument('user_id', type=str, location='json', required=True)
        args = parse.parse_args()

        user_id = args['user_id']

        return update_user(user_id)

    @jwt_required()
    def delete(self, user_id):
        """
        HTTP DELETE. Delete an user.
        :returns:
        """
        return delete_user(user_id)


users_api_blueprint = Blueprint('users_api_blueprint', __name__)
user_api = CustomApi(users_api_blueprint)

user_api.add_resource(UsersAPI, '/', endpoint='user_list')
user_api.add_resource(UserAPI, '<user_id>', endpoint='user_detail')
