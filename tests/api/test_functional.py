# -*- coding: utf-8 -*-
"""Functional tests using WebTest"""
from flask import url_for
import pytest
from tests.factories import UserFactory, AdminFactory
from flask_api.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from flask_jwt import _default_jwt_encode_handler
from webtest.app import AppError


@pytest.mark.usefixtures('db')
@pytest.mark.usefixtures('jwt')
class TestUserApi:
    """User related functionality."""

    def test_unauthorized_get_users(self, testapp):
        """Tests the GET /users endpoint"""
        try:
            res = testapp.request(url_for('users_api_blueprint.list'), method='GET')
            assert res.status_code == HTTP_401_UNAUTHORIZED
        except AppError as e:
            assert '401' in e.args[0]

    def test_get_users(self, testapp):
        """Tests the GET /users endpoint"""
        UserFactory().save()
        admin = AdminFactory()
        admin.save()
        token = _default_jwt_encode_handler(admin).decode('utf-8')
        res = testapp.request(url_for('users_api_blueprint.list'), method='GET',
                              headers={'Authorization': 'Bearer %s' % token})
        assert res.status_code == HTTP_200_OK
        assert len(res.json['data']) > 1

    def test_unauthorized_get_user_me(self, testapp):
        """Tests the GET /users endpoint"""
        try:
            res = testapp.request(url_for('users_api_blueprint.me'), method='GET')
            assert res.status_code == HTTP_401_UNAUTHORIZED
        except AppError as e:
            assert '401' in e.args[0]

    def test_get_user_me(self, testapp):
        """Tests the GET /users endpoint"""
        admin = AdminFactory()
        admin.save()
        token = _default_jwt_encode_handler(admin).decode('utf-8')
        res = testapp.request(url_for('users_api_blueprint.me'), method='GET',
                              headers={'Authorization': 'Bearer %s' % token})
        assert res.status_code == HTTP_200_OK
        assert res.json['data']['attributes']['email'] == admin.email
