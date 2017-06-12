"""
config.py

configure parameters for RumahNumeroUno Webapp
1. secret key for form
2. email
"""

import os

# location of project folder
basedir = os.path.abspath(os.path.dirname(__file__))

# parent class Config
class Config:
    # secret_key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SSL
    SSL_DISABLE = True
    # JAKARTA API TOKEN
    JAKARTA_API_TOKEN = os.environ.get('JAKARTA_API_TOKEN')

    @staticmethod
    def init_app(app):
        pass

# configuration for development, subclass of Config
class DevelopmentConfig(Config):
    DEBUG = True

# additional config for Heroku deployment
class HerokuConfig(Config):
    SSL_DISABLE=bool(os.environ.get('SSL_DISABLE'))

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)


# dict mapping
config = {
    'development': DevelopmentConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
