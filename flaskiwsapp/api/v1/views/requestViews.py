from flask.blueprints import Blueprint
from flask_restful import Resource
from flask_jwt import jwt_required
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.api.v1.schemas.requestSchemas import RequestJsonSchema

requests_api_blueprint = Blueprint('requests_api_blueprint', __name__)
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
        request_schema = RequestJsonSchema(many=True)

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


request_api.add_resource(RequestsAPI, '/', endpoint='list')
request_api.add_resource(RequestAPI, '<request_id>', endpoint='detail')
