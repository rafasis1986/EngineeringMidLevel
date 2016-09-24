from flask.blueprints import Blueprint
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flaskiwsapp.snippets.customApi import CustomApi
from flaskiwsapp.api.v1.schemas.targetSchemas import TargetJsonSchema


def post_put_parser():
    """
    Request parser for HTTP POST or PUT.

    :returns: flask.ext.restful.reqparse.RequestParser object
    """
    parse = reqparse.RequestParser()
    parse.add_argument('email', type=str, location='json', required=True)
    parse.add_argument('password', type=str, location='json', required=True)

    return parse


class TargetsAPI(Resource):
    """An API to get or create targets."""

    @jwt_required()
    def get(self, email=None):
        """HTTP GET. Get one or all targets.

        :email: a string valid as object id.
        :returns: One or all available targets.

        """

        targets = get_all_targets()
        target_schema = TargetJsonSchema(many=True)

        return target_schema.dump(targets).data


class TargetAPI(Resource):
    """An API to update or delete an target. """

    @jwt_required()
    def put(self, target_id):
        """
        HTTP PUT. Update an target.
        :returns:
        """

        parse = post_put_parser()
        parse.add_argument('target_id', type=str, location='json', required=True)
        args = parse.parse_args()

        target_id = args['target_id']

        return update_target(target_id)

    @jwt_required()
    def delete(self, target_id):
        """
        HTTP DELETE. Delete an target.
        :returns:
        """
        return delete_target(target_id)


targets_api_blueprint = Blueprint('targets_api_blueprint', __name__)
target_api = CustomApi(targets_api_blueprint)

target_api.add_resource(TargetsAPI, '/', endpoint='target_list')
target_api.add_resource(TargetAPI, '<target_id>', endpoint='target_detail')
