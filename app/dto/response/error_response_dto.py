"""
Error response data transfer object.
"""
from app.dto.response.base_response_dto import BaseResponseDTO

class ErrorResponseDTO(BaseResponseDTO):
    """
    Data transfer object for error responses.
    
    Attributes:
        reason (str): The reason for the error.
        success (bool): Whether the operation was successful.
    """
    def __init__(self, reason: str, success: bool = False):
        super().__init__(success)
        self.reason = reason

    def to_dict(self):
        return {
            'reason': self.reason,
            'success': self.success
        }
