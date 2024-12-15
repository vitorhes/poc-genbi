from dataclasses import dataclass
from ...domain.entities import PromptStatus
from ...domain.value_objects import RequestId, ResultURL
from ...domain.types import ProcessingError
from ..interfaces.repository import IPromptRequestRepository

@dataclass
class UpdateStatusUseCase:
    """Use case for updating prompt request status."""
    
    repository: IPromptRequestRepository

    def execute(self, request_id: RequestId, status: PromptStatus, result_url: ResultURL = None) -> None:
        """Update the status of a prompt request."""
        try:
            self.repository.update_status(request_id, status, result_url)
        except Exception as e:
            raise ProcessingError(f"Failed to update status: {str(e)}") 