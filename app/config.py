# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   config.py
@Time    :   2022/06/22 14:49:39
@Author  :   zzyyww
@Version :   1.0
@Desc    :   None
"""

import os


class BASE_CONFIG:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DEV_CONFIG(BASE_CONFIG):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345@127.0.0.1:3306/labeldata"
    REDIS_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_BROKER_URL = REDIS_URL
    CELERYD_HIJACK_ROOT_LOGGER = False
    CELERYD_MAX_TASKS_PER_CHILD = 1


class PRO_CONFIG(BASE_CONFIG):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345@127.0.0.1:3306/labeldata"
    REDIS_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_BROKER_URL = REDIS_URL
    CELERYD_HIJACK_ROOT_LOGGER = False
    CELERYD_MAX_TASKS_PER_CHILD = 1


class TEST_CONFIG(BASE_CONFIG):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345@127.0.0.1:3306/labeldata"
    REDIS_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_BROKER_URL = REDIS_URL
    CELERYD_HIJACK_ROOT_LOGGER = False
    CELERYD_MAX_TASKS_PER_CHILD = 1


def fetch_cfg(config_name=os.getenv('FLASK_ENV', 'dev')):
    if config_name.lower() == 'dev':
        return DEV_CONFIG()
    if config_name.lower() == 'pro':
        return PRO_CONFIG()
    if config_name.lower() == 'test':
        return TEST_CONFIG()
