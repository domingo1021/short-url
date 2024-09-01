from flask import Blueprint, jsonify
from flasgger import swag_from

from app.type.typed_response import TypedResponse
from app.dto.request.shorten_api_request_dto import ShortenApiRequestDTO
from app.dto.response.shorten_api_response_dto import ShortenApiResponseDTO
from app.utils.validator import validate_request

url_api = Blueprint('url_api', __name__)

@swag_from('../../docs/shorten_api.yml')
@url_api.route('/shorten', methods=['POST'])
@validate_request(ShortenApiRequestDTO)
async def shorten_url(dto: ShortenApiRequestDTO) -> TypedResponse[ShortenApiResponseDTO]:
    original_url = dto.original_url

    short = ShortenApiResponseDTO(original_url)

    return jsonify(short.to_dict())