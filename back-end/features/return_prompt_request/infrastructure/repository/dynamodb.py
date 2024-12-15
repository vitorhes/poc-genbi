from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from ...application.interfaces.repository import IPromptRequestRepository
from ...domain.entities import PromptStatus
from ...domain.value_objects import RequestId, ResultURL

class PromptRequestModel(Model):
    """PynamoDB model for prompt requests."""
    class Meta:
        table_name = 'prompt-requests'
        region = 'us-east-1'  # Configure as needed
        
    request_id = UnicodeAttribute(hash_key=True)
    status = UnicodeAttribute()
    result_url = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute()

class DynamoDBRepository(IPromptRequestRepository):
    """DynamoDB implementation of prompt request repository using PynamoDB."""
    
    def update_status(self, request_id: RequestId, status: PromptStatus, result_url: ResultURL = None) -> None:
        """Update prompt request status in DynamoDB."""
        try:
            prompt_request = PromptRequestModel.get(request_id.value)
            
            # Update attributes
            prompt_request.status = status.value
            if result_url:
                prompt_request.result_url = result_url.value
                
            prompt_request.save()
            
        except PromptRequestModel.DoesNotExist:
            raise ValueError(f"Prompt request with id {request_id.value} not found") 