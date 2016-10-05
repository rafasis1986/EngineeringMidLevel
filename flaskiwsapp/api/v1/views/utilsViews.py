'''
Created on Oct 5, 2016

@author: rtorres
'''
from flask.blueprints import Blueprint
from flask_cors.extension import CORS
from flask_jwt import jwt_required
from flaskiwsapp.projects.snippets.constants import AREAS
from flask.json import jsonify

utils_api_blueprint = Blueprint('utils_api_blueprint', __name__)
cors = CORS(utils_api_blueprint)


@utils_api_blueprint.route('areas', endpoint='areas')
@jwt_required()
def areas():
    areas = list()
    for item in AREAS:
        areas.append({'name': item})
    return jsonify(areas)
