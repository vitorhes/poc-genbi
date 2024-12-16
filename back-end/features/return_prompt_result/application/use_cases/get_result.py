from dataclasses import dataclass
from ...domain.entities import PromptResult, PromptStatus, LLMResponse, PromptRequest
from ...domain.value_objects import RequestId
from ..interfaces.repository import IPromptRequestRepository
from ..interfaces.storage import IStorageService


@dataclass
class GetResultUseCase:
    """Use case for getting processing results."""
    
    repository: IPromptRequestRepository
    storage_service: IStorageService

    def execute(self, request_id: RequestId) -> PromptResult:
        """
        Get the result for a specific request ID.
        
        Args:
            request_id: The ID of the request
            
        Returns:
            PromptResult: The result of the prompt
        """
        # Get result metadata from repository
        prompt_request: PromptRequest = self.repository.get_prompt_request(request_id)
        
        # If status is completed, fetch content from storage
        if prompt_request.status == PromptStatus.COMPLETED:
            llm_response: LLMResponse = self.storage_service.get_result(prompt_request.result_url)

            return PromptResult(
                request_id = request_id,
                llm_response = llm_response.value,
                result_url = prompt_request.result_url,
                status = prompt_request.status,
         
            )
            
        return prompt_request
