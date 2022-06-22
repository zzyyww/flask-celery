# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   testController.py
@Time    :   2022/06/22 15:00:12
@Author  :   zzyyww
@Version :   1.0
@Desc    :   None
"""
from flask import jsonify


def test():
    return jsonify({"status": "ok"})
