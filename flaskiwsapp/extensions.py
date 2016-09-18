# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py"""
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Brypt
bcrypt = Bcrypt()

# Database/SQLAlchemy/Migrations
db = SQLAlchemy()
migrate = Migrate()

# JWT
jwt = None

# Marshmallow
ma = Marshmallow()

###############################
# Login manager configuration #
###############################

login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "warning"
