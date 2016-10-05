from werkzeug.exceptions import BadRequest

from flask import request
from flask.blueprints import Blueprint
from flask_cors.extension import CORS
from flask_jwt import jwt_required, current_identity, JWTError
from flask_restful import Resource, reqparse, fields, marshal_with

from flaskiwsapp.api.v1.schemas.ticketSchemas import BaseTicketJsonSchema
from flaskiwsapp.projects.controllers.requestControllers import get_request_by_id
from flaskiwsapp.projects.controllers.ticketControllers import create_ticket, delete_ticket, \
    get_ticket_by_id, get_tickets_user, get_all_tickets
from flaskiwsapp.snippets.customApi import CustomApi


tickets_api_blueprint = Blueprint('tickets_api_blueprint', __name__)
cors = CORS(tickets_api_blueprint)
tickets_api = CustomApi(tickets_api_blueprint)


ticket_parser = reqparse.RequestParser(bundle_errors=True)
ticket_parser.add_argument('request_id', type=int, location='json', required=True, help="Choose a request id")
ticket_parser.add_argument('detail', type=str, location='json', required=True, help="send a detail.")

ticket_fields = {
    'request_id': fields.Integer,
    'detail': fields.String
}


class TicketsAPI(Resource):
    """An API to get or create tickets."""

    @jwt_required()
    def get(self):
        """
        HTTP GET. Get all requests.

        :email: a string valid as object id.
        :returns: One or all available requests.

        """
        tickets = get_all_tickets()
        request_schema = BaseTicketJsonSchema(many=True)
        return request_schema.dump(tickets).data

    @jwt_required()
    @marshal_with(ticket_fields)
    def post(self):
        try:
            args = ticket_parser.parse_args()
            request = get_request_by_id(args.request_id)
            ticket = create_ticket(request, current_identity, args.detail)
            ticket_schema = BaseTicketJsonSchema()
        except BadRequest as e:
            raise JWTError(e, e.description)
        except Exception as e:
            raise JWTError(e, e.args[0])
        else:
            ticket = get_ticket_by_id(ticket.id)
            return ticket_schema.dump(ticket).data


class TicketAPI(Resource):
    """An API to get or delete a ticket. """

    @jwt_required()
    def delete(self, ticket_id):
        """
        HTTP DELETE. Delete an ticket.
        :returns:
        """
        return delete_ticket(ticket_id)

    @jwt_required()
    def get(self, ticket_id):
        """
        HTTP DELETE. Get specific Ticket.
        :returns:
        """
        ticket = get_ticket_by_id(ticket_id)
        return BaseTicketJsonSchema().dump(ticket).data


class TicketMeAPI(Resource):
    """An API to get me tickets. """

    @jwt_required()
    def get(self):
        tickets = get_tickets_user(current_identity.id)
        return BaseTicketJsonSchema(many=True).dump(tickets).data

tickets_api.add_resource(TicketsAPI, '', endpoint='list')
tickets_api.add_resource(TicketMeAPI, 'me', endpoint='me')
tickets_api.add_resource(TicketAPI, '<ticket_id>', endpoint='detail')
