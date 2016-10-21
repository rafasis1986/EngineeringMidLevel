"""Admin views."""

from flask import redirect, url_for, abort
from flask.globals import request
from flask_admin import expose, helpers
from flask_admin.contrib import sqla

import flask_admin as admin
import flask_login as login
from flaskiwsapp.admin.forms import AdminLoginForm, AdminUserForm
from flaskiwsapp.auth.snippets.authExceptions import AuthBaseException
from flaskiwsapp.auth.snippets.dbconections import auth0_user_signup, \
    auth0_user_change_password
from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flaskiwsapp.users.validators import get_user
from flaskiwsapp.projects.controllers.requestControllers import insert_request_priority,\
    remove_request_from_priority_list, update_request_on_priority_list, update_checked_request
from flaskiwsapp.workers.queueManager import create_request_sms_job, create_ticket_sms_job,\
    create_ticket_email_job, create_welcome_user_email_job
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired, URL


# Create customized model view class
class MyModelView(sqla.ModelView):
    create_modal = True
    edit_modal = True

    def is_accessible(self):
        return login.current_user.is_authenticated and login.current_user.is_admin

    def _handle_view(self, name, **kwargs):
        """
        Override builtin handle_view in order to redirect users when a
        view is not accessible.
        """
        if not self.is_accessible():
            abort(404)


# Create customized view for user models
class UserView(MyModelView):
    """Flask user model view."""
    form = AdminUserForm
    list_template = 'admin/users/list.html'
    column_searchable_list = ('email', 'phone_number', 'id')

    def after_model_change(self, form, model, is_created):
        # Set password if password_dummy is set
        try:
            if (form.password_dummy.data != '' and form.password_dummy.data is not None):
                model.set_password(form.password_dummy.data)
                if is_created:
                    auth0_user_signup(form.email.data, form.password_dummy.data)
                    create_welcome_user_email_job(model.id)
                else:
                    auth0_user_change_password(form.email.data, form.password_dummy.data)
        except (BaseIWSExceptions, AuthBaseException):
            self.session.rollback()


class RequestView(MyModelView):
    """Flask Request model view."""
    list_template = 'admin/request/list.html'
    form_excluded_columns = ('ticket_url')
    column_searchable_list = ('client_id', 'product_area', 'client_priority', 'target_date')

    # Add dummy password field
    form_extra_fields = {
        'url_dummy': StringField('Ticket url', validators=[DataRequired(), URL()])
    }
    form_columns = (
        'title',
        'description',
        'client',
        'client_priority',
        'product_area',
        'url_dummy',
        'target_date'
    )

    def on_model_change(self, form, model, is_created):
        MyModelView.on_model_change(self, form, model, is_created)
        model.ticket_url = form.url_dummy.data

    def after_model_change(self, form, model, is_created):
        MyModelView.after_model_change(self, form, model, is_created)
        if is_created:
            model = insert_request_priority(model)
            create_request_sms_job(model.id)
        else:
            model = update_request_on_priority_list(model)

    def on_model_delete(self, model):
        MyModelView.after_model_delete(self, model)
        model = remove_request_from_priority_list(model)


class TicketView(MyModelView):
    """Flask Request model view."""
    form_columns = (
        'request',
        'user',
        'detail'
    )
    column_searchable_list = ('user_id', 'request_id', 'created_at')

    def after_model_change(self, form, model, is_created):
        MyModelView.after_model_change(self, form, model, is_created)
        request = update_checked_request(model.request.id)
        create_ticket_sms_job(model.id)
        create_ticket_email_job(model.id)


# Create customized index view class taht handles login & registration
class MyAdminIndexView(admin.AdminIndexView):
    """
    Flask Admin view. Only Users with the 'is_admin' flag
    have access.
    """

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = AdminLoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = get_user(form)
            login.login_user(user)
        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.login_view'))
