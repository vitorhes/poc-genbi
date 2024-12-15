from dataclasses import dataclass
from ...domain.types import ProcessingError
from ...domain.value_objects import RequestId, ResultContent, ResultURL
from ..interfaces.storage import IStorageService

@dataclass
class SaveResultUseCase:
    """Use case for saving processing results."""
    
    storage_service: IStorageService

    def execute(self, request_id: RequestId, result_content: ResultContent) -> ResultURL:
        """
        Save the processed result to storage.
        
        Returns:
            ResultURL: URL of the saved result
        """
        try:
            return self.storage_service.save_result(request_id, result_content)
        except Exception as e:
            raise ProcessingError(f"Failed to save result: {str(e)}") 