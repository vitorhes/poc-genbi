# back-end/features/return_prompt_result/application/interfaces/storage.py
from typing import Protocol
from ...domain.value_objects import LLMResponse, ResultURL

class IStorageService(Protocol):
    """Interface for storage services."""
    def get_result(self, url: ResultURL) -> LLMResponse:
        """Get result from storage."""
        pass