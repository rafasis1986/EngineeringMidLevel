from flask import jsonify
from flask.blueprints import Blueprint
from flask_api.status import HTTP_202_ACCEPTED, HTTP_206_PARTIAL_CONTENT
from flask_cors.extension import CORS
from flask_jwt import jwt_required, current_identity, JWTError
from flask_restful import Resource, reqparse

from flaskiwsapp.api.v1.schemas.userSchemas import UserDetailJsonSchema, BaseUserJsonSchema
from flaskiwsapp.snippets.cache import get_client_phone_cache, save_client_phone_cache
from flaskiwsapp.snippets.constants import ROLE_CLIENT
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.snippets.exceptions.baseExceptions import LogicalException
from flaskiwsapp.snippets.exceptions.userExceptions import UserPhoneNotAvaliableException
from flaskiwsapp.snippets.helpers import roles_required
from flaskiwsapp.snippets.logger import iws_logger, MSG_ERROR
from flaskiwsapp.users.controllers.userControllers import get_all_users, update_user, is_an_available_phone
from flaskiwsapp.workers.queueManager import create_confirm_sms_job, create_confirm_email_job
from werkzeug.exceptions import BadRequest
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException


users_api_blueprint = Blueprint('users_api_blueprint', __name__)
cors = CORS(users_api_blueprint)
users_api = CustomApi(users_api_blueprint)
phone_parser = reqparse.RequestParser(bundle_errors=True)
phone_parser.add_argument('phone_number', type=str, location='json', required=True, help="Send phone number")
code_parser = reqparse.RequestParser(bundle_errors=True)
code_parser.add_argument('code', type=str, location='json', required=True, help="Send code")


class UsersAPI(Resource):
    """An API to get or create users."""

    @jwt_required()
    def get(self, email=None):
        """
        HTTP GET. Get one or all users.

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

    @jwt_required()
    @roles_required(ROLE_CLIENT)
    def put(self):
        try:
            args = code_parser.parse_args()
            phone = get_client_phone_cache(current_identity.id, args.code)
        except LogicalException as e:
            iws_logger.error(MSG_ERROR % (type(e), e.message))
            raise JWTError(e, e.message)
        except BadRequest as e:
            msg = ''.join('{}: {};'.format(key, val) for key, val in e.data.get('message').items())
            iws_logger.error(MSG_ERROR % (type(e), msg))
            raise JWTError(e, e.description)
        except Exception as e:
            iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
            raise JWTError(e, e.args[0])
        else:
            iws_logger.info('Code confirm success to client %s' % current_identity.id)
            client = update_user(current_identity.id, {'phone_number': phone})
            return UserDetailJsonSchema().dump(client).data, HTTP_202_ACCEPTED

    @jwt_required()
    @roles_required(ROLE_CLIENT)
    def patch(self):
        args = phone_parser.parse_args()
        if not is_an_available_phone(args.phone_number):
            e = UserPhoneNotAvaliableException(args.phone_number)
            iws_logger.error(MSG_ERROR % (type(e), e.message))
            raise JWTError(e, e.message)
        try:
            phone = phonenumbers.parse(args.phone_number, None)
        except NumberParseException as e:
            iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
            raise JWTError(e, e.args[0])
        else:
            key = save_client_phone_cache(current_identity.id, args.phone_number)
            task_email = create_confirm_email_job(current_identity.id, key)
            task_sms = create_confirm_sms_job(current_identity.id, key)
            iws_logger.info('We sent confirmations sms %s and email %s to user %s' % (task_sms, task_email, current_identity.id))
            return {'message': 'please verify the code in your phone or email'}, HTTP_206_PARTIAL_CONTENT


users_api.add_resource(UsersAPI, '', endpoint='list')
users_api.add_resource(UserMeAPI, 'me', endpoint='me')
