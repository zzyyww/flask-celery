# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/06/22 14:48:49
@Author  :   zzyyww
@Version :   1.0
@Contact :   605921814@qq.com
@Desc    :   None
"""

from flask import Flask
from flask_migrate import Migrate

from app.celerys import create_celery_app
from app.models import db

from .config import fetch_cfg

celery_app = None
cfg = None


def create_app(config_name):
    global celery_app, cfg
    app = Flask(__name__)
    cfg = fetch_cfg(config_name)
    app.config.from_object(cfg)
    db.init_app(app)
    Migrate(app, db)

    celery_app = create_celery_app(app)
    from app.routes import api
    app.register_blueprint(api)

    return app
