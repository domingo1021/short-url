"""
This file is responsible for creating the blueprint for the URL shortening API.
"""
from flask import Blueprint

from app.controller.url_controller import shorten_url, redirect_url
from app.type.http import HttpMethods

url_bp = Blueprint('shorten', __name__)

url_bp.route('/shorten', methods=[HttpMethods.POST.value])(shorten_url)
url_bp.route('/redirect/<short_url_code>', methods=[HttpMethods.GET.value])(redirect_url)
