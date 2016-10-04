'''
Created on Sep 23, 2016

@author: rtorres
'''
from flask.helpers import url_for


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


def get_api_urls(app):
    res = dict()
    res.update({'user_list': url_for('users_api_blueprint.list')})
    res.update({'client_list': url_for('clients_api_blueprint.list')})
    res.update({'request_list': url_for('requests_api_blueprint.list')})
    res.update({'tickets_list': url_for('tickets_api_blueprint.list')})
    str_resp = ''
    for k in res.keys():
        str_resp += k + ':' + res[k] + ';'
    return str_resp
