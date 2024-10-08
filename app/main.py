"""
This module provides the main entry point for the Flask application.

It sets up the Flask app, registers blueprints, and configures the Swagger generator.
"""
from flask import Flask, jsonify

from app.api.url import url_bp
from app.utils.swagger import SwaggerGenerator
from app.dto.response.error_response_dto import ErrorResponseDTO
from app.type.http import HttpStatusCode
from app.utils.limiter import limiter

def resource_not_found(_):
    """
    Function to handle 404 errors.
    """
    error = ErrorResponseDTO('Resource not found')
    return jsonify(error.to_dict()), HttpStatusCode.NOT_FOUND.value

def too_many_request(_):
    """
    Function to handle 429 errors.
    """
    error = ErrorResponseDTO('Too many requests')
    return jsonify(error.to_dict()), HttpStatusCode.TOO_MANY_REQUESTS.value

def internal_server_error(error):
    """
    Function to handle 500 errors.
    """
    print("Unexpected error:", error)
    error = ErrorResponseDTO('Internal server error')
    return jsonify(error.to_dict()), HttpStatusCode.INTERNAL_SERVER_ERROR.value

def create_app() -> Flask:
    """
    Function to create the Flask app, and add all components to it.
    """
    app = Flask(__name__)

    app.register_blueprint(url_bp)
    app.register_error_handler(HttpStatusCode.NOT_FOUND.value, resource_not_found)
    app.register_error_handler(HttpStatusCode.TOO_MANY_REQUESTS.value, too_many_request)
    app.register_error_handler(HttpStatusCode.INTERNAL_SERVER_ERROR.value, internal_server_error)
    SwaggerGenerator.config(app)

    limiter.init_app(app)

    return app

if __name__ == '__main__':
    main_app = create_app()
    main_app.run()
