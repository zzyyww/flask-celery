from flask import Flask
from flask_migrate import Migrate

from app.celerys import create_celery_app
from app.models import db

from .config import fetch_cfg