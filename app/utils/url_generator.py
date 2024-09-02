"""
Short URL Generator
"""
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

class ShortUrlGenerator:
    """Short URL Generator class."""

    REDIRECT_BASE_URL = BASE_URL + 'redirect/'
    SHORT_URL_LENGTH = 6

    @staticmethod
    def generate_url(original_url: str, salt: str = '') -> str:
        """Generate a short URL with md5 hash."""
        hashed_url = hashlib.md5((original_url + salt).encode()).hexdigest()
        short_url = hashed_url[:ShortUrlGenerator.SHORT_URL_LENGTH]
        return ShortUrlGenerator.REDIRECT_BASE_URL + short_url
