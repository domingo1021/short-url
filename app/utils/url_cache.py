"""
URL Cache Utils that interact short URLs with Redis.
"""
from redis.client import Pipeline

from app.utils.redis_client import redis_client
from app.utils.url_generator import ShortUrlGenerator

SHORT_URL_PREFIX = 'short_url:'
ORIGIN_URL_PREFIX = 'origin_url:'

class UrlCache:
    """
    URL Cache contains static method the help cache and retrieve short URLs in Redis.
    """
    @staticmethod
    def cache_urls(short_url: str, original_url: str, ttl: int, pipe: Pipeline = None) -> None:
        """ Cache the short URL in Redis. """
        short_url = short_url.replace(ShortUrlGenerator.REDIRECT_BASE_URL, '')
        short_url_key = SHORT_URL_PREFIX + short_url
        original_url_key = ORIGIN_URL_PREFIX + original_url

        cache = pipe or redis_client
        cache.setex(name=short_url_key, value=original_url, time=ttl)
        cache.setex(name=original_url_key, value=short_url, time=ttl)

    @staticmethod
    def get_short_url(original_url: str) -> str:
        """ Get the short URL from Redis. """
        return redis_client.get(ORIGIN_URL_PREFIX + original_url)

    @staticmethod
    def url_exists(short_url: str) -> bool:
        """ Check if the short URL exists in Redis. """
        return redis_client.exists(SHORT_URL_PREFIX + short_url)
