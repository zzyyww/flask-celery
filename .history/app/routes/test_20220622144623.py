from flask import Blueprint, abort, current_app, jsonify, request
from flask_httpauth import HTTPTokenAuth

api = Blueprint('api', __name__, url_prefix='api')


def test():
    return jsonify({'status': "ok"})
