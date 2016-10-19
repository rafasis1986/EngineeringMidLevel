'''
Created on Sep 23, 2016

@author: rtorres
'''
import random
import string

from flask.helpers import url_for
from flaskiwsapp.users.controllers.roleControllers import get_role_by_name
from flaskiwsapp.snippets.constants import ROLE_EMPLOYEE, ROLE_CLIENT


def split_name(name):
    name = name.strip()
    pivot = name.rfind(' ')
    if pivot > 0:
        first_name = name[:pivot]
        last_name = name[pivot + 1:]
    else:
        first_name = name
        last_name = ''
    return first_name, last_name


def get_api_urls(app, user):
    res = dict()
    role1 = get_role_by_name(ROLE_EMPLOYEE)
    role2 = get_role_by_name(ROLE_CLIENT)
    if role1 in user.roles:
        res.update({'client_list': url_for('clients_api_blueprint.list')})
        res.update({'request_list': url_for('requests_api_blueprint.list')})
        res.update({'tickets_list': url_for('tickets_api_blueprint.list')})
    elif role2 in user.roles:
        res.update({'request_list': url_for('requests_api_blueprint.me')})
        res.update({'tickets_list': url_for('clients_api_blueprint.tickets')})
        res.update({'pending_list': url_for('requests_api_blueprint.pending')})
    res.update({'user_list': url_for('users_api_blueprint.list')})
    res.update({'utils_areas': url_for('utils_api_blueprint.areas')})
    str_resp = ''
    for k in res.keys():
        str_resp += k + ':' + res[k] + ';'
    return str_resp


def set_enviroment(app):
    env = dict()
    env.update({'AUTH0_CLIENT_ID': app.config['AUTH0_CLIENT_ID']})
    env.update({'AUTH0_DOMAIN': app.config['AUTH0_DOMAIN']})
    env.update({'AUTH0_CALLBACK_URL': app.config['AUTH0_CALLBACK_URL']})
    env.update({'AUTH0_CALLBACK_EMP_URL': app.config['AUTH0_CALLBACK_EMP_URL']})
    return env


def make_payload(app, code, call_back_url):
    return {'client_id': app.config['AUTH0_CLIENT_ID'],
            'client_secret': app.config['AUTH0_CLIENT_SECRET'],
            'redirect_uri': call_back_url,
            'code': code,
            'grant_type': 'authorization_code'}


def generate_key(length=8):
    ret = []
    for i in range(0, length):
        ret.extend(random.sample(string.hexdigits, 1))
    return ''.join(ret)
