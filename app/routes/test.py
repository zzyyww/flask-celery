# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   test.py
@Time    :   2022/06/22 14:48:43
@Author  :   zzyyww
@Version :   1.0
@Desc    :   None
"""

from app.controller.testController import test
from flask import Blueprint, abort, current_app, jsonify, request
from flask_httpauth import HTTPTokenAuth

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test', methods=["post"])
def test_api():
    return test()
    # return jsonify({'status': "ok"})
