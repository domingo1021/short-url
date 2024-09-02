"""
Define shortening API request DTO, validate the request with Pydantic, and use it in the controller.
"""
from pydantic import BaseModel, Field
from app.utils.url_generator import ShortUrlGenerator as SU

class RedirectApiRequestDTO(BaseModel):
    """
    DTO for the URL shortening API request in declarative form.
    """
    short_url_code: str = Field(..., min_length=SU.SHORT_URL_LENGTH ,max_length=SU.SHORT_URL_LENGTH)
