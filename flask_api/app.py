from db import db
from flask import Flask
from flask_smorest import Api
from resources.houseslima import blp as Propertiesblueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    # Iniating the database
    db.init_app(app)

    # Connecting flask-smorest with the app
    api = Api(app)
    api.register_blueprint(Propertiesblueprint)

    return app


