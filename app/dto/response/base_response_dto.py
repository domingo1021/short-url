"""
Module for the Abstract BaseResponseDTO class.
"""
from abc import ABC, abstractmethod
from typing import Dict

class BaseResponseDTO(ABC):
    """ Abstract base class for all response DTOs. """
    success: bool

    def __init__(self, success: bool):
        self.success = success

    @abstractmethod
    def to_dict(self) -> Dict:
        """ Convert the DTO to a dictionary. """
