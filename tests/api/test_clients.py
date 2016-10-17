# -*- coding: utf-8 -*-
"""Functional tests using WebTest"""
from flask import url_for
import pytest
from tests.factories import AdminFactory, ClientFactory, RoleEmployeeFactory, RoleClientFactory, UserFactory
from flask_api.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from flask_jwt import _default_jwt_encode_handler
from webtest.app import AppError


@pytest.mark.usefixtures('db')
@pytest.mark.usefixtures('jwt')
class TestClientApi:
    """User related functionality."""

    def test_unauthorized_get_clients(self, testapp):
        """Tests the GET /clients endpoint"""
        try:
            res = testapp.request(url_for('clients_api_blueprint.list'), method='GET')
            assert res.status_code == HTTP_401_UNAUTHORIZED
        except AppError as e:
            assert '401' in e.args[0]

    def test_get_clients(self, testapp):
        """Tests the GET /clients endpoint"""
        c = ClientFactory().save()
        role = RoleClientFactory().save()
        c.roles.append(role)
        c.save()
        user = UserFactory().save()
        role = RoleEmployeeFactory().save()
        user.roles.append(role)
        user.save()
        admin = AdminFactory()
        admin.save()
        token = _default_jwt_encode_handler(user).decode('utf-8')
        res = testapp.request(url_for('clients_api_blueprint.list'), method='GET',
                              headers={'Authorization': 'Bearer %s' % token})
        assert res.status_code == HTTP_200_OK
        assert len(res.json['data']) > 0
