import os
from db import db
from flask import Flask
from flask_smorest import Api
from resources.houseslima import blp as Propertiesblueprint


def create_app(db_url=None):
    app = Flask(__name__)

    # Config
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Houses Lima Database API"
    app.config["API_VERSION"] = "v1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL",'sqlite:///data.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    

    # Iniating the database
    db.init_app(app)

    # Connecting flask-smorest with the app
    api = Api(app)
    api.register_blueprint(Propertiesblueprint)

    return app


