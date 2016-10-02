from flask.blueprints import Blueprint
from flask_cors.extension import CORS
from flask_jwt import jwt_required
from flask_restful import Resource

from flaskiwsapp.api.v1.schemas.requestSchemas import BaseRequestJsonSchema, RequestDetailJsonSchema
from flaskiwsapp.projects.controllers.requestControllers import get_all_requests, update_request, delete_request,\
    get_request_by_id
from flaskiwsapp.snippets.customApi import CustomApi


requests_api_blueprint = Blueprint('requests_api_blueprint', __name__)
cors = CORS(requests_api_blueprint)
request_api = CustomApi(requests_api_blueprint)


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
    def put(self, request_id):
        """
        HTTP PUT. Update an target.
        :returns:
        """

        return update_request(request_id)

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


request_api.add_resource(RequestsAPI, '/', endpoint='list')
request_api.add_resource(RequestAPI, '<request_id>', endpoint='detail')
