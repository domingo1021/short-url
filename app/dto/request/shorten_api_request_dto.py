from pydantic import BaseModel, Field

MAX_URL_LENGTH = 2048

class ShortenApiRequestDTO(BaseModel):
    original_url: str = Field(..., max_length=MAX_URL_LENGTH)