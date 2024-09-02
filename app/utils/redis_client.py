"""
Redis client connection model that connects to the Redis server.
"""
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

ORIGIN_URL_PREFIX = 'original:'
SHORT_URL_PREFIX = 'short:'
