from flask import Response, jsonify
from typing import Generic, TypeVar

# Define a generic type variable
T = TypeVar('T')

class TypedResponse(Response, Generic[T]):
    def __init__(self, data: T, *args, **kwargs):
        self.data: T = data
        super().__init__(response=jsonify(data), *args, **kwargs)