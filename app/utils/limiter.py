"""
Rate limit configuration for the URL shortening and redirecting APIs.
"""
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.utils.redis_client import REDIS_HOST, REDIS_PORT

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=f"redis://{REDIS_HOST}:{REDIS_PORT}"
)
