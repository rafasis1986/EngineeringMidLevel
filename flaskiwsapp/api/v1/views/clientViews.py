from flask.blueprints import Blueprint
from flask_cors.extension import CORS
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource

from flaskiwsapp.api.v1.schemas.clientSchemas import ClientDetailJsonSchema, BaseClientJsonSchema
from flaskiwsapp.snippets.constants import ROLE_EMPLOYEE, ROLE_CLIENT
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.snippets.helpers import roles_required, is_admin_user
from flaskiwsapp.users.controllers.clientControllers import get_all_clients, get_client_by_id
from flaskiwsapp.users.controllers.userControllers import delete_user
from flaskiwsapp.api.v1.schemas.ticketSchemas import BaseTicketJsonSchema
from flaskiwsapp.projects.controllers.ticketControllers import get_tickets_by_client


clients_api_blueprint = Blueprint('clients_api_blueprint', __name__)
cors = CORS(clients_api_blueprint)
client_api = CustomApi(clients_api_blueprint)


class ClientsAPI(Resource):
    """An API to get or create clients."""

    @jwt_required()
    @roles_required(ROLE_EMPLOYEE)
    def get(self):
        """
        HTTP GET. Get one or all clients.

        :email: a string valid as object id.
        :returns: One or all available clients.

        """
        clients = get_all_clients()
        client_schema = BaseClientJsonSchema(many=True)

        return client_schema.dump(clients).data


class ClientAPI(Resource):
    """An API to update or delete an client. """

    @jwt_required()
    @is_admin_user
    def delete(self, client_id):
        """
        HTTP DELETE. Delete an client.
        :returns:
        """
        return delete_user(client_id)

    @jwt_required()
    @roles_required(ROLE_EMPLOYEE)
    def get(self, client_id):
        """
        HTTP GET Clients details
        :returns:
        """
        client = get_client_by_id(client_id)
        return ClientDetailJsonSchema().dump(client).data


class ClientMeTicketsAPI(Resource):
    """An API to get all clients request. """

    @jwt_required()
    @roles_required(ROLE_CLIENT)
    def get(self):
        """
        HTTP GET Client Requests pending
        :returns: json object
        """
        requests = get_tickets_by_client(current_identity.id)
        return BaseTicketJsonSchema(many=True).dump(requests).data

client_api.add_resource(ClientsAPI, '', endpoint='list')
client_api.add_resource(ClientMeTicketsAPI, 'me/tickets', endpoint='tickets')
client_api.add_resource(ClientAPI, '<client_id>', endpoint='detail')
