from flask import Flask
from flasgger import Swagger

class SwaggerGenerator:
    @staticmethod
    def config(app: Flask) -> None:
        app.config['SWAGGER'] = {
            'title': 'Short URL API',
            'uiversion': 3
        }
        Swagger(app)