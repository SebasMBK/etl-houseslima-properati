import os

PROPAGATE_EXCEPTIONS = True
API_TITLE = "Houses Lima Database API"
API_VERSION = "v1.0"
OPENAPI_VERSION = "3.0.3"
OPENAPI_URL_PREFIX = "/"
OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL",'sqlite:///data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False