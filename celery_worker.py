#!/usr/bin/env python
import os

from flaskiwsapp.settings.devConfig import DevConfig
from flaskiwsapp.settings.prodConfig import ProdConfig
from flaskiwsapp.app import create_app
from flaskiwsapp.extensions import celery

CONFIG = ProdConfig if os.environ.get('IWS_BE') == 'prod' else DevConfig

app = create_app(CONFIG)
app.app_context().push()
