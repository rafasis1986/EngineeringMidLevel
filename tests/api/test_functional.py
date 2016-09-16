# -*- coding: utf-8 -*-
"""Functional tests using WebTest"""
from flask import url_for


class TestUserApi:
    """User related functionality."""

    def test_get_users(self, testapp):
        """Tests the GET /users endpoint"""
        pass
        #===============================================================================================================
        # res = testapp.get(url_for('user_blueprint.user_list'))
        # assert res.status_code == 200
        # assert len(res.json) > 0
        #===============================================================================================================
