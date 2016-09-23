import base64

from flask import request, session, redirect, render_template
from flask.blueprints import Blueprint
import requests

import json
from flask.globals import current_app
import datetime


auth_blueprint = Blueprint('auth',__name__,)


@auth_blueprint.route('/')
def login():
    env = dict()
    env.update({'AUTH0_CLIENT_ID': current_app.config['AUTH0_CLIENT_ID']})
    env.update({'AUTH0_DOMAIN': current_app.config['AUTH0_DOMAIN']})
    env.update({'AUTH0_CALLBACK_URL': current_app.config['AUTH0_CALLBACK_URL']})
    return render_template('auth/login.html', env=env)


@auth_blueprint.route('/callback/')
def call_back():
    code = request.args.get('code')
    json_header = {'content-type': 'application/json'}
    token_url = "https://{domain}/oauth/token".format(domain=current_app.config['AUTH0_DOMAIN'])
    token_payload = {
        'client_id': current_app.config['AUTH0_CLIENT_ID'],
        'client_secret': current_app.config['AUTH0_CLIENT_SECRET'],
        'redirect_uri': current_app.config['AUTH0_CALLBACK_URL'],
        'code': code,
        'grant_type': 'authorization_code'
    }
    token_info = requests.post(token_url, data=json.dumps(token_payload), headers=json_header).json()
    user_url = "https://{domain}/userinfo?access_token={access_token}" \
        .format(domain=current_app.config['AUTH0_DOMAIN'], access_token=token_info['access_token'])

    user_info = requests.get(user_url).json()
    response_url = current_app.config['APP_URL']
    response = redirect(response_url, code=302)
    expire_date = datetime.datetime.now() + current_app.config['JWT_EXPIRATION_DELTA']
    response.set_cookie('Authorization', value='123', expires=expire_date)
    return response
