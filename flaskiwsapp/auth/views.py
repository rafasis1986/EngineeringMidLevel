
import datetime
import json
import requests

from flask import request, redirect, render_template
from flask.blueprints import Blueprint
from flask.globals import current_app
from flask_jwt import _default_jwt_encode_handler
from flaskiwsapp.snippets.utils import split_name, set_enviroment, make_payload, make_auth_response
from flaskiwsapp.users.controllers.userControllers import is_an_available_email, update_user, get_employee_by_email
from flaskiwsapp.users.controllers.clientControllers import create_client, get_client_by_email
from flaskiwsapp.snippets.exceptions.userExceptions import EmployeeDoesNotExistsException, UserDoesNotExistsException
from flaskiwsapp.snippets.logger import iws_logger, MSG_ERROR


auth_blueprint = Blueprint('auth', __name__,)


@auth_blueprint.route('/')
def login():
    env = set_enviroment(current_app)
    return render_template('auth/login.html', env=env)


@auth_blueprint.route('callback/')
def call_back():
    code = request.args.get('code')
    json_header = {'content-type': 'application/json'}
    token_url = "https://{domain}/oauth/token".format(domain=current_app.config['AUTH0_DOMAIN'])
    token_payload = make_payload(current_app, code, current_app.config['AUTH0_CALLBACK_URL'])
    token_info = requests.post(token_url, data=json.dumps(token_payload), headers=json_header).json()
    user_url = "https://{domain}/userinfo?access_token={access_token}" \
        .format(domain=current_app.config['AUTH0_DOMAIN'], access_token=token_info['access_token'])
    user_info = requests.get(user_url).json()
    try:
        if is_an_available_email(user_info.get('email')):
            user = create_client(user_info['email'], None)
            iws_logger.info('Client %s sign up success' % user_info.get('email'))
        else:
            user = get_client_by_email(user_info.get('email'))
            iws_logger.info('Client %s login success' % user_info.get('email'))
    except UserDoesNotExistsException as e:
        env = set_enviroment(current_app)
        iws_logger.error(MSG_ERROR % (type(e), e.message))
        return render_template('auth/login.html', error='Check your credentials', env=env)
    else:
        social = user_info['identities'][0]['connection']
        social_id = user_info['identities'][0]['user_id']
        if 'google' in social:
            first_name = user_info['given_name']
            last_name = user_info['family_name']
        else:
            first_name, last_name = split_name(user_info['name'])
        user = update_user(user.id, {'social': social,
                                     'social_id': social_id,
                                     'first_name': first_name,
                                     'last_name': last_name})
        token = _default_jwt_encode_handler(user)
        response_url = current_app.config['APP_URL']
        response = redirect(response_url, code=302)
        expire_date = datetime.datetime.now() + current_app.config['JWT_EXPIRATION_DELTA']
        response = make_auth_response(current_app, response, user, token, expire_date)
        return response


@auth_blueprint.route('callback/emp')
def call_back_employee():
    code = request.args.get('code')
    json_header = {'content-type': 'application/json'}
    token_url = "https://{domain}/oauth/token".format(domain=current_app.config['AUTH0_DOMAIN'])
    token_payload = make_payload(current_app, code, current_app.config['AUTH0_CALLBACK_EMP_URL'])
    token_info = requests.post(token_url, data=json.dumps(token_payload), headers=json_header).json()
    user_url = "https://{domain}/userinfo?access_token={access_token}" \
        .format(domain=current_app.config['AUTH0_DOMAIN'], access_token=token_info['access_token'])
    user_info = requests.get(user_url).json()
    try:
        user = get_employee_by_email((user_info.get('email')))
    except EmployeeDoesNotExistsException as e:
        env = set_enviroment(current_app)
        iws_logger.error(MSG_ERROR % (type(e), e.message))
        return render_template('auth/login.html', error='Employee does not exists', env=env)
    except Exception as e:
        env = set_enviroment(current_app)
        iws_logger.error(MSG_ERROR % (type(e), e.args[0]))
        return render_template('auth/login.html', env=env)
    else:
        iws_logger.info('Employee %s login success' % user_info.get('email'))
        social = user_info['identities'][0]['connection']
        social_id = user_info['identities'][0]['user_id']
        if 'google' in social:
            first_name = user_info['given_name']
            last_name = user_info['family_name']
        else:
            first_name, last_name = split_name(user_info['name'])
        user = update_user(user.id, {'social': social,
                                     'social_id': social_id,
                                     'first_name': first_name,
                                     'last_name': last_name})
        token = _default_jwt_encode_handler(user)
        response_url = current_app.config['APP_URL']
        response = redirect(response_url, code=302)
        expire_date = datetime.datetime.now() + current_app.config['JWT_EXPIRATION_DELTA']
        response = make_auth_response(current_app, response, user, token, expire_date)
        return response
