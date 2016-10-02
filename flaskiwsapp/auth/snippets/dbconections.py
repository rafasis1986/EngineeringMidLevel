'''
Created on Sep 22, 2016

@author: rtorres
'''
import requests
import json

from flask.globals import current_app
from flaskiwsapp.auth.snippets.authExceptions import AuthUpdateException,\
    AuthSignUpException


def auth0_user_signup(email, password, kwargs={}):
    template_url = 'https://%s/dbconnections' % current_app.config['AUTH0_DOMAIN']
    url = template_url + '/signup'
    payload = {'client_id': current_app.config['AUTH0_CLIENT_ID'],
               'email': email,
               'password': password,
               'connection': current_app.config['APP_NAME'],
               'user_metadata': kwargs
               }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response_dic = json.loads(response.text)
    if 'error' in response_dic.keys():
        raise AuthSignUpException(response_dic.get('error'))
    return response_dic


def auth0_user_change_password(email, password, kwargs={}):
    template_url = 'https://%s/dbconnections' % current_app.config['AUTH0_DOMAIN']
    url = template_url + '/change_password'
    payload = {'client_id': current_app.config['AUTH0_CLIENT_ID'],
               'email': email,
               'password': password,
               'connection': current_app.config['APP_NAME']
               }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response_dic = json.loads(response.text)
    if 'error' in response_dic.keys():
        raise AuthUpdateException(response_dic.get('error'))
    return json.loads(response.text)
