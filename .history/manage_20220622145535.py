# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   manage.py
@Time    :   2022/06/22 14:49:44
@Author  :   zzyyww
@Version :   1.0
@Desc    :   None
"""
import logging
import os

from flask_cors import CORS

from app import create_app
from app.logConfig import setup_logging

app = create_app(os.environ.get("FLASK_ENV", "pri"))
from app import celery_app

# root = logging.getLogger()

setup_logging()

# from app.models import db

CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run()