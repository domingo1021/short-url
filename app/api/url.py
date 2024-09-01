"""
This file is responsible for creating the blueprint for the URL shortening API.
"""
from flask import Blueprint

from app.controller.shorten_url_controller import shorten_url

url_bp = Blueprint('shorten', __name__)

url_bp.route('/shorten', methods=['POST'])(shorten_url)
