"""
Redis client connection model that connects to the Redis server.
"""
import os
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
ORIGIN_URL_PREFIX = 'original:'
SHORT_URL_PREFIX = 'short:'

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
