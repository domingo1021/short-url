"""
Shorten URL Controller
"""
from flask import jsonify
from flasgger import swag_from

from app.type.typed_response import TypedResponse
from app.dto.request.shorten_api_request_dto import ShortenApiRequestDTO
from app.dto.response.shorten_api_response_dto import ShortenApiResponseDTO
from app.utils.validator import validate_request


@swag_from('../../docs/shorten_api.yml')
@validate_request(ShortenApiRequestDTO)
async def shorten_url(dto: ShortenApiRequestDTO) -> TypedResponse[ShortenApiResponseDTO]:
    """
    Presentational layer for the URL shortening API.

    :param dto: The request DTO, will be validated by the "ShortenApiRequestDTO" shcema.
    :return: The response data transfer object.
    """
    original_url = dto.original_url

    short = ShortenApiResponseDTO(original_url)

    return jsonify(short.to_dict())
