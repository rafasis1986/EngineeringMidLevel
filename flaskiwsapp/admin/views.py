"""Admin views."""
from flask import redirect, url_for, abort
from flask_admin import expose
from flask_admin.contrib import sqla
from wtforms import PasswordField

import flask_admin as admin
import flask_login as login
from flaskiwsapp.auth.snippets.dbconections import auth0_user_signup,\
    auth0_user_change_password
from flaskiwsapp.auth.snippets.authExceptions import AuthSignUpException,\
    AuthUpdateException
from flaskiwsapp.users.controllers import update_user_password
from flaskiwsapp.snippets.exceptions.baseExceptions import BaseIWSExceptions
from flask.helpers import flash
from _locale import gettext


# Create customized model view class
class MyModelView(sqla.ModelView):

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
    create_modal = True
    edit_modal = True

    # Remove password field from form
    form_excluded_columns = ('password')

    # Add dummy password field
    form_extra_fields = {
        'password_dummy': PasswordField('Password')
    }

    # Set the form fields to use
    form_columns = (
        'email',
        'first_name',
        'last_name',
        'password_dummy',
        'created_at',
        'active',
        'is_admin'
    )

    def on_model_change(self, form, User, is_created):
        # Set password if password_dummy is set
        try:
            if (form.password_dummy.data != '' and form.password_dummy.data is not None):
                user = update_user_password(User.id, form.password_dummy.data)
        except BaseIWSExceptions as e:
            return False

    def create_model(self, form):
        """
            Create model from form.
 
            :param form:
                Form instance
        """
        try:
            auth0_user_signup(form.email.data, form.password_dummy.data)
        except AuthSignUpException:
            self.session.rollback()
            return False
        return MyModelView.create_model(self, form)
 
    def update_model(self, form, model):
        """
            Update model from form.
 
            :param form:
                Form instance
            :param model:
                Model instance
        """
        try:
            auth0_user_change_password(form.email.data, form.password_dummy.data)
        except AuthUpdateException:
            self.session.rollback()
            return False
        return MyModelView.update_model(self, form, model)


# Create customized index view class taht handles login & registration
class MyAdminIndexView(admin.AdminIndexView):
    """Flask Admin view. Only Users with the 'is_admin' flag
    have access."""

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
