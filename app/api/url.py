"""
This file is responsible for creating the blueprint for the URL shortening API.
"""
from flask import Blueprint

from app.controller.url_controller import shorten_url
from app.type.http_mehotd import POST

url_bp = Blueprint('shorten', __name__)

url_bp.route('/shorten', methods=[POST])(shorten_url)
