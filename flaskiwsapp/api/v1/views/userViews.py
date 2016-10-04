from flask.blueprints import Blueprint
from flask_cors.extension import CORS
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse

from flaskiwsapp.api.v1.schemas.userSchemas import UserDetailJsonSchema, BaseUserJsonSchema
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.users.controllers.userControllers import get_all_users


users_api_blueprint = Blueprint('users_api_blueprint', __name__)
cors = CORS(users_api_blueprint)
users_api = CustomApi(users_api_blueprint)


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
        user_schema = BaseUserJsonSchema(many=True)
        return user_schema.dump(users).data


class UserMeAPI(Resource):
    """An API to use me info """

    @jwt_required()
    def get(self):
        """
        HTTP GET. show myself info
        :returns:
        """
        return UserDetailJsonSchema().dump(current_identity).data


users_api.add_resource(UsersAPI, '', endpoint='list')
users_api.add_resource(UserMeAPI, 'me', endpoint='me')
