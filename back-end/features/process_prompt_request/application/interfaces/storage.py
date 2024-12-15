from ...domain.value_objects import RequestId, ResultContent
from typing import Protocol


class IStorageService(Protocol):
    """Interface for storage services."""
    
    def save_result(self, request_id: RequestId, result_content: ResultContent) -> str:
        """Save result and return the URL."""
        pass 