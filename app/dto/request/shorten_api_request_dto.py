"""
Define shortening API request DTO, validate the request with Pydantic, and use it in the controller.
"""
from pydantic import BaseModel, Field, AnyUrl

MAX_URL_LENGTH = 2048

class ShortenApiRequestDTO(BaseModel):
    """
    DTO for the URL shortening API request in declarative form.
    """
    original_url: AnyUrl = Field(..., max_length=MAX_URL_LENGTH)
