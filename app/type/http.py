"""
A constant file that contains the HTTP
"""
from enum import Enum

POST = 'POST'
GET = 'GET'

class HttpStatusCode(Enum) :
    """
    Class to represent HTTP status codes.
    """
    OK = 200
    REDIRECT = 302
    BAD_REQUEST = 400
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
