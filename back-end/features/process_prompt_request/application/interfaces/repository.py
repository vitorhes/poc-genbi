from typing import Protocol
from ...domain.entities import PromptStatus
from ...domain.value_objects import RequestId, ResultURL

class IPromptRequestRepository(Protocol):
    """Interface for prompt request repository."""
    
    def update_status(
            self,
            request_id: RequestId,
            status: PromptStatus,
            result_url: ResultURL = None
            ) -> None:
        """Update prompt request status."""
        pass 