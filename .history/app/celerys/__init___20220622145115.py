# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/06/22 14:48:17
@Author  :   zzyyww
@Version :   1.0
@Desc    :   None
"""

from celery import Celery


def create_celery_app(app=None):
    '''
    Create a new Celery object and tie together the Celery config to the app's
    '''
    celery_app = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery_app.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask

    return celery_app
