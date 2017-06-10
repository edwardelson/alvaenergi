"""
/app

configure app/ with config.py
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config

# initialize objects
moment = Moment()
bootstrap = Bootstrap()


# create application
def create_app(config_name):
    app = Flask(__name__)
    # run additional init_app from Config class
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initialize objects with config.py
    bootstrap.init_app(app)
    moment.init_app(app)

    # call Blueprint from main/
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # redirect requests to secure HTTP
    # enable only in production mode
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    return app
