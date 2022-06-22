import logging

from flask import has_request_context, request


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.method = request.method
            record.remote_addr = request.remote_addr
            if request.method == 'GET':
                record.data = request.args
            else:
                record.data = request.json
        else:
            record.url = None
            record.method = None
            record.remote_addr = None
            record.data = {}
        return super().format(record)


class CeleryFormatter(logging.Formatter):
    '''celery日志格式'''
    def format(self, record):
        from celery._state import get_current_task
        task = get_current_task()
        if task and task.request:
            record.__dict__.update(task_id=task.request.id, task_name=task.name)
        else:
            record.__dict__.setdefault('task_name', '')
            record.__dict__.setdefault('task_id', '')
        return super().format(record)
