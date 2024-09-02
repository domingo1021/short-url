"""
URL Controller
"""
from flask import jsonify
from flasgger import swag_from

from app.type.typed_response import TypedResponse
from app.dto.request.shorten_api_request_dto import ShortenApiRequestDTO
from app.dto.response.shorten_api_response_dto import ShortenApiResponseDTO
from app.utils.validator import validate_request
from app.services.shorten_url_service import ShortenUrlService


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
