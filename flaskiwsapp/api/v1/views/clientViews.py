from flask.blueprints import Blueprint
from flask_restful import Resource
from flaskiwsapp.users.controllers.clientControllers import get_all_clients, delete_client, get_client_by_id
from flask_jwt import jwt_required
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.api.v1.schemas.clientSchemas import ClientJsonSchema
from flask_cors.extension import CORS


clients_api_blueprint = Blueprint('clients_api_blueprint', __name__)
cors = CORS(clients_api_blueprint)
client_api = CustomApi(clients_api_blueprint)


class ClientsAPI(Resource):
    """An API to get or create clients."""

    @jwt_required()
    def get(self, email=None):
        """HTTP GET. Get one or all clients.

        :email: a string valid as object id.
        :returns: One or all available clients.

        """

        clients = get_all_clients()
        client_schema = ClientJsonSchema(many=True)

        return client_schema.dump(clients).data


class ClientAPI(Resource):
    """An API to update or delete an client. """

    @jwt_required()
    def delete(self, client_id):
        """
        HTTP DELETE. Delete an client.
        :returns:
        """
        return delete_client(client_id)

    @jwt_required()
    def get(self, client_id):
        """
        HTTP DELETE. Delete an client.
        :returns:
        """
        client = get_client_by_id(client_id)
        return ClientJsonSchema().dump(client).data


client_api.add_resource(ClientsAPI, '/', endpoint='list')
client_api.add_resource(ClientAPI, '<client_id>', endpoint='detail')
