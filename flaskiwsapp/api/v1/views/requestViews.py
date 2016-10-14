from flask.blueprints import Blueprint
from flask_cors.extension import CORS
from flask_jwt import jwt_required, JWTError, current_identity
from flask_restful import Resource, reqparse, fields

from flaskiwsapp.api.v1.schemas.requestSchemas import BaseRequestJsonSchema, RequestDetailJsonSchema
from flaskiwsapp.projects.controllers.requestControllers import get_all_requests, delete_request,\
    get_request_by_id, create_request, get_client_pending_requests
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.users.controllers.clientControllers import get_client_by_id
from dateutil import parser
from flask import jsonify
from flaskiwsapp.workers.queueManager import create_request_sms_job


requests_api_blueprint = Blueprint('requests_api_blueprint', __name__)
cors = CORS(requests_api_blueprint)
request_api = CustomApi(requests_api_blueprint)

request_parser = reqparse.RequestParser(bundle_errors=True)

request_parser.add_argument('client_priority', type=str, location='json', required=True, help="Send priority")
request_parser.add_argument('details', type=str, location='json', required=True, help="send a details")
request_parser.add_argument('ticket_url', type=str, location='json', required=True, help="send a ticket_url")
request_parser.add_argument('product_area', type=str, location='json', required=True, help="send product_area")
request_parser.add_argument('title', type=str, location='json', required=True, help="send a title")
request_parser.add_argument('target_date', type=str, location='json', required=True, help="send a datetime")

ticket_fields = {
    'client': fields.String,
    'client_priority': fields.String,
    'details': fields.String,
    'product_area': fields.String,
    'target_date': fields.String,
    'ticket_url': fields.String,
    'title': fields.String
}


class RequestsAPI(Resource):
    """An API to get or create requests."""

    @jwt_required()
    def get(self):
        """HTTP GET. Get one or all requests.

        :email: a string valid as object id.
        :returns: One or all available requests.

        """
        requests = get_all_requests()
        request_schema = BaseRequestJsonSchema(many=True)

        return request_schema.dump(requests).data


class RequestAPI(Resource):
    """An API to update or delete an request. """

    @jwt_required()
    def delete(self, request_id):
        """
        HTTP DELETE. Delete an request.
        :returns:
        """
        return delete_request(request_id)

    @jwt_required()
    def get(self, request_id):
        """
        HTTP DELETE. Get specific Request.
        :returns:
        """
        request = get_request_by_id(request_id)
        return RequestDetailJsonSchema().dump(request).data


class RequestsMeAPI(Resource):
    """An API to get or create requests by a client."""

    @jwt_required()
    def get(self):
        """HTTP GET. Get one or all requests.

        :email: a string valid as object id.
        :returns: One or all available requests.

        """
        requests = get_client_pending_requests(current_identity.id)
        request_schema = BaseRequestJsonSchema(many=True)

        return request_schema.dump(requests).data

    @jwt_required()
    def post(self):
        try:
            response = None
            client = get_client_by_id(current_identity.id)
            args = request_parser.parse_args()
            date = parser.parse(args.target_date)
            req_dict = dict()
            req_dict.update({'title': args.title})
            req_dict.update({'description': args.details})
            req_dict.update({'ticket_url': args.ticket_url})
            req_dict.update({'client': client})
            req_dict.update({'client_priority': int(args.client_priority)})
            req_dict.update({'product_area': args.product_area})
            req_dict.update({'target_date': date})
            request = create_request(req_dict)
            request_schema = RequestDetailJsonSchema()
            response = request_schema.dump(get_request_by_id(request.id)).data
            create_request_sms_job(request.id)
        except BadRequest as e:
            raise JWTError(e, e.description)
        except Exception as e:
            raise JWTError(e, e.args[0])
        else:
            return jsonify(response)

    @jwt_required()
    def delete(self, request_id):
        """
        HTTP DELETE. Delete an request.
        :returns:
        """
        return delete_request(request_id)


request_api.add_resource(RequestsAPI, '', endpoint='list')
request_api.add_resource(RequestAPI, '<request_id>', endpoint='detail')
request_api.add_resource(RequestsMeAPI, 'me', endpoint='me')
