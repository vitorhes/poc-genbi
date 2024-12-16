# back-end/features/return_prompt_result/application/interfaces/repository.py
from typing import Protocol
from ...domain.entities import PromptRequest
from ...domain.value_objects import RequestId

class IPromptRequestRepository(Protocol):
    """Interface for result repository."""
    def get_prompt_request(self, request_id: RequestId) -> PromptRequest:
        """Get a prompt request from repository."""
        pass