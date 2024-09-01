"""
This module provides the main entry point for the Flask application.

It sets up the Flask app, registers blueprints, and configures the Swagger generator.
"""
from flask import Flask

from app.api.url import url_bp
from app.utils.swagger import SwaggerGenerator

def create_app():
    """
    Function to create the Flask app, and add all components to it.
    """
    app = Flask(__name__)

    app.register_blueprint(url_bp)
    SwaggerGenerator.config(app)

    return app

main_app = create_app()
