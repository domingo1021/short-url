"""
Shorten URL Service that implement the business logic for the URL shortening API.
"""
from app.models.url_mapping import UrlMapping
from app.utils.url_shortener_orchestor import UrlShortenerOrchestrator

class ShortenUrlService:
    """Shorten URL Service that implement the business logic for the URL shortening API."""
    @staticmethod
    def generate_short_url(original_url) -> UrlMapping:
        """
        Generate short url and store it in Redis.

        :param original_url: The original URL.
        :return: The short URL object
        """
        url = UrlMapping(original_url=original_url)
        UrlShortenerOrchestrator.get_or_create_short_url(url)

        return url
