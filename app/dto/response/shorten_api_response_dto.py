from app.dto.response.base_response_dto import BaseResponseDTO

class ShortenApiResponseDTO(BaseResponseDTO):
    def __init__(self, short_url: str):
        self.short_url = short_url

    def to_dict(self):
        return {
            'short_url': self.short_url
        }