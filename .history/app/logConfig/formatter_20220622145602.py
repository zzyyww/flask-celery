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
