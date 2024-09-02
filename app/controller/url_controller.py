"""
URL Controller
"""
import os
from flask import jsonify, redirect, Response
from flasgger import swag_from
from dotenv import load_dotenv
from pydantic import ValidationError

from app.type.typed_response import TypedResponse
from app.dto.request.shorten_api_request_dto import ShortenApiRequestDTO
from app.dto.request.redirect_api_request_dto import RedirectApiRequestDTO
from app.dto.response.shorten_api_response_dto import ShortenApiResponseDTO
from app.utils.validator import validate_request_body
from app.services.shorten_url_service import ShortenUrlService
from app.dto.response.error_response_dto import ErrorResponseDTO
from app.type.http import HttpStatusCode
from app.utils.limiter import limiter

load_dotenv()
docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'docs'))

@swag_from(os.path.join(docs_dir, 'shorten_api.yml'))
@validate_request_body(ShortenApiRequestDTO)
@limiter.limit("10 per minute")
def shorten_url(request_dto: ShortenApiRequestDTO) -> TypedResponse[ShortenApiResponseDTO]:
    """
    Presentational layer for the URL shortening API.

    :param dto: The request DTO, will be validated by the "ShortenApiRequestDTO" shcema.
    :return: The response data transfer object.
    """
    original_url = str(request_dto.original_url)

    url = ShortenUrlService.generate_short_url(original_url)
    response_dto = ShortenApiResponseDTO(short_url=url.short_url, expiration_date=url.expiration_date)

    return jsonify(response_dto.to_dict())

@swag_from(os.path.join(docs_dir, 'redirect_api.yml'))
@limiter.limit("1 per second")
def redirect_url(short_url_code: str) -> Response:
    """
    Presentational layer for the URL redirecting API.

    :param short_url: The short URL to redirect to.
    :return: The redirect response.
    """
    try:
        RedirectApiRequestDTO(short_url_code=short_url_code)
    except ValidationError as e:
        error = ErrorResponseDTO(e.json())
        return jsonify(error.to_dict()), HttpStatusCode.BAD_REQUEST.value

    complete_short_url = os.getenv('BASE_URL') + 'redirect/' + short_url_code
    print(f"Redirecting to short URL {complete_short_url}")

    original_url = ShortenUrlService.get_original_url(complete_short_url)
    if not original_url:
        error = ErrorResponseDTO(f"Original URL not found for the given short URL {complete_short_url}")
        return jsonify(error.to_dict()), HttpStatusCode.NOT_FOUND.value

    return redirect(original_url)
