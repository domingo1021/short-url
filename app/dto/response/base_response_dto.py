from abc import ABC, abstractmethod
from typing import Dict

class BaseResponseDTO(ABC):
    @abstractmethod
    def to_dict(self) -> Dict:
        pass