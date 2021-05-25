import os
import importlib

import click
from flask import Flask, Blueprint

from .models import *
from .settings import config
from .extensions import db,  migrate


def create_app(config_name=None):
    if config_name is None:
        config_name = 'development'
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    Register(app)
    return app


class Register:

    def __init__(self, app):
        self.extensions(app)
        self.blueprint(app)
        self.commands(app)
        self.error_handlers(app)
        self.shell_context(app)

    @staticmethod
    def extensions(app):
        # db.init_app(app)
        migrate.init_app(app, db)

    @staticmethod
    def blueprint(app, blueprints_dirname='api'):
        blueprints_path = os.path.join(app.root_path, blueprints_dirname)
        import_str = f'{app.name}.{blueprints_dirname}.'
        for item in [py_file for py_file in os.listdir(blueprints_path) if py_file.endswith('.py')]:
            bp_module = importlib.import_module(import_str + os.path.splitext(item)[0])
            for var_name in dir(bp_module):
                var = getattr(bp_module, var_name)
                if isinstance(var, Blueprint):
                    app.register_blueprint(var)

    @staticmethod
    def commands(app):
        @app.cli.command()
        def test_command():
            click.echo('test command success.')

    @staticmethod
    def error_handlers(app):
        @app.errorhandler(404)
        def page_not_found(e):
            return {'code': 1, 'msg': '一不小心走丢啦'}, 404

    @staticmethod
    def shell_context(app):
        @app.shell_context_processor
        def make_shell_context():
            return dict(db=db)
