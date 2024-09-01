from flask import Flask

from app.api.url import url_api
from app.utils.swagger import SwaggerGenerator

def create_app():
    app = Flask(__name__)

    app.register_blueprint(url_api)
    SwaggerGenerator.config(app)

    return app

app = create_app()
