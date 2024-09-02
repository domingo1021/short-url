"""
ShortenApiResponseDTO is a class that represents the response of the shorten API.
"""
from app.dto.response.base_response_dto import BaseResponseDTO

class ShortenApiResponseDTO(BaseResponseDTO):
    """
    Data transfer object for the shorten API response.
    """
    def __init__(self, short_url: str, expiration_date: str, success: bool = True):
        super().__init__(success)
        self.short_url = short_url
        self.expiration_date = expiration_date

    def to_dict(self):
        return {
            'short_url': self.short_url,
            'expiration_date': self.expiration_date,
            'success': super().success
        }
