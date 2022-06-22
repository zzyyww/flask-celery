from flask import Flask
from flask_migrate import Migrate

from app.celerys import create_celery_app
from app.models import db

from .config import fetch_cfg

celery_app = None
cfg = None


def create_app(config_name):
    global celery_app, cfg
    app = Flask(__name__)
    cfg = fetch_cfg(config_name)
    app.config.from_object(cfg)
    db.init_app(app)
    Migrate(app, db)

    celery_app = create_celery_app(app)
    from app.routes import api
    app.register_blueprint(api)

    return app
