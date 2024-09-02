"""
URL Controller
"""
import os
from flask import jsonify, redirect, Response
from flasgger import swag_from
from dotenv import load_dotenv

from app.type.typed_response import TypedResponse
from app.dto.request.shorten_api_request_dto import ShortenApiRequestDTO
from app.dto.response.shorten_api_response_dto import ShortenApiResponseDTO
from app.utils.validator import validate_request
from app.services.shorten_url_service import ShortenUrlService
from app.dto.response.error_response_dto import ErrorResponseDTO
from app.type.http import HttpStatusCode

load_dotenv()

@swag_from('../../docs/shorten_api.yml')
@validate_request(ShortenApiRequestDTO)
def shorten_url(request_dto: ShortenApiRequestDTO) -> TypedResponse[ShortenApiResponseDTO]:
    """
    Presentational layer for the URL shortening API.

    :param dto: The request DTO, will be validated by the "ShortenApiRequestDTO" shcema.
    :return: The response data transfer object.
    """
    original_url = request_dto.original_url

    url = ShortenUrlService.generate_short_url(original_url)
    response_dto = ShortenApiResponseDTO(short_url=url.short_url, expiration_date=url.expiration_date)

    return jsonify(response_dto.to_dict())

@swag_from('../../docs/redirect_api.yml')
def redirect_url(short_url: str) -> Response:
    """
    Presentational layer for the URL redirecting API.

    :param short_url: The short URL to redirect to.
    :return: The redirect response.
    """
    complete_short_url = os.getenv('BASE_URL') + 'redirect/' + short_url
    print(f"Redirecting to short URL {complete_short_url}")

    original_url = ShortenUrlService.get_original_url(short_url)
    if not original_url:
        error = ErrorResponseDTO(f"Original URL not found for the given short URL {complete_short_url}")
        return jsonify(error.to_dict()), HttpStatusCode.NOT_FOUND.value

    return redirect(original_url)
