import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
# from flask import request
# from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Incorporating the Blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.formsubmit import bp as formsubmit_bp
    app.register_blueprint(formsubmit_bp)

    # ------- #
    # Logging #
    # ------- #
    # This section handles logging setup
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')

    return app


# from app import models
