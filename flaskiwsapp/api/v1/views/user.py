from flaskiwsapp.api.v1.controllers import user as UserController
from flaskiwsapp.snippets import helpers
from flaskiwsapp.users.models import User
from flask.blueprints import Blueprint
from flask_restful import Api, Resource
from flask_restful import reqparse, fields, marshal_with

API_VERSION = '1.0'

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/api')
user_api = Api(user_blueprint)

user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument('username', type=str, required=True, help="Choose a username. It needs to be unique.")
user_parser.add_argument('email', type=str, required=True, help="Choose a email. It needs to be unique.")
user_parser.add_argument('password', type=str, required=True, help="Choose a password")

# This will be used to marshal output for users
user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String
}


@user_blueprint.after_request
def additional_info(response):
    response.headers['API-Version'] = API_VERSION
    return response


class UserListResource(Resource):
    """
    This is API endpoint resource for `users` as collection.
    All operations performed here will be for the `users collection`.
    """

    @marshal_with(user_fields)
    def get(self, username=None):
        return UserController.get_users(username)

    @marshal_with(user_fields)
    def post(self):
        args = user_parser.parse_args()
        user = User(username=args.username, email=args.email, password=args.password).save()
        user_url = fields.Url('user_blueprint.user_detail', absolute=True)
        user_url = user_url.output(user_url.endpoint, {"username": user.username})
        return user, 201, {"Location": user_url}


class UserDetailResource(Resource):

    @marshal_with(user_fields)
    def get(self, username=None):
        if username:
            return User.query.filter_by(username=username).first()

    def patch(self, id):
        user = User.query.get(id)
        if not user:
            abort(404, message="User does not exist")
        return {"patch": "Implementation pending"}, 501

user_api.add_resource(UserListResource, '/', endpoint='user_list')
user_api.add_resource(UserDetailResource, '<username>', endpoint='user_detail')