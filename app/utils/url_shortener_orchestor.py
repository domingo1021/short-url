"""
URL Shortener Orchestrator module, generates and stores short URLs in Redis.
"""
from datetime import datetime, timezone
import redis

from app.utils.url_cache import UrlCache, SHORT_URL_PREFIX
from app.utils.url_generator import ShortUrlGenerator
from app.models.url_mapping import UrlMapping
from app.utils.redis_client import redis_client

class UrlShortenerOrchestrator:
    """
    URL Shortener Orchestrator class, which is responsible orchestrating the URL shortening process.
    """

    @staticmethod
    def get_original_url(short_url: str) -> str | None:
        """
        Get the original URL from the short URL.
        """

        original_url = UrlCache.get_original_url(short_url)
        if original_url:
            print(f"Original URL {original_url} found in cache.")
            return original_url.decode()

        return None

    @staticmethod
    def get_or_create_short_url(url_mapping: UrlMapping) -> str:
        """
        Get or create a short URL for the given URL mapping, and store it in Redis.
        """

        ttl = int((url_mapping.expiration_date - datetime.now(timezone.utc)).total_seconds())

        short_url = UrlCache.get_short_url(url_mapping.original_url)
        if short_url:
            short_url = ShortUrlGenerator.REDIRECT_BASE_URL + short_url.decode()
            UrlCache.cache_urls(short_url, url_mapping.original_url, ttl)
            print(f"Short URL {short_url} already exists in cache.")
            return short_url

        print(f"Generating new short URL for {url_mapping.original_url}")
        while True:
            short_url = ShortUrlGenerator.generate_url(url_mapping.original_url)
            try:
                with redis_client.pipeline() as pipe:
                    pipe.watch(SHORT_URL_PREFIX + short_url)

                    if UrlCache.url_exists(short_url):
                        time_salt = str(datetime.now().timestamp())
                        short_url = ShortUrlGenerator.generate_url(url_mapping.original_url, salt=time_salt)
                        pipe.unwatch()
                        continue

                    pipe.multi()
                    UrlCache.cache_urls(short_url, url_mapping.original_url, ttl, pipe)
                    pipe.execute()
                    break

            except redis.WatchError:
                pipe.reset()
                continue

        return short_url
