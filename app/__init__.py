import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import DevelopmentConfig

db = SQLAlchemy()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    from app.order_history import order_history_api
    from app.routes import api

    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(order_history_api, url_prefix="/api")

    return app
