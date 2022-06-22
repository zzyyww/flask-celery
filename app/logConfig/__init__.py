# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/06/22 14:59:08
@Author  :   zzyyww
@Version :   1.0
@Desc    :   None
"""

from logging.config import dictConfig

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'flask_formatter': {
            'format':
            '%(asctime)s - flask - %(remote_addr)s - %(method)s - %(data)s - %(url)s - %(levelname)s - %(lineno)s - %(module)s - %(funcName)s - %(message)s',
            'class': 'app.logConfig.formatter.RequestFormatter'
        },
        'celery_formatter': {
            'format': "%(asctime)s - celery - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s",
            'class': 'app.logConfig.formatter.CeleryFormatter'
        }
    },
    'handlers': {
        'flask_handler': {
            'level': 'INFO',
            'formatter': 'flask_formatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './log/data.log',
            'maxBytes': 10485760,
            'backupCount': 10,
            'encoding': 'utf8',
        },
        'celery_handler': {
            'level': 'INFO',
            'formatter': 'celery_formatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './log/data.log',
            'maxBytes': 10485760,
            'backupCount': 10,
            'encoding': 'utf8',
        },
    },
    'loggers': {
        'celery_logger': {
            'handlers': ['celery_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery.task': {
            'handlers': ['celery_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery.worker': {
            'handlers': ['celery_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'app': {
            'handlers': ['flask_handler'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


def setup_logging():
    dictConfig(LOG_CONFIG)
