
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from ...domain.entities import PromptStatus, PromptRequest
from ...domain.value_objects import RequestId, ResultURL 
from ...application.interfaces.repository import IPromptRequestRepository

class PromptRequestModel(Model):
    """PynamoDB model for prompt requests."""
    class Meta:
        table_name = 'prompt-requests'
        region = 'us-east-1'
        
    request_id = UnicodeAttribute(hash_key=True)
    status = UnicodeAttribute()
    result_url = UnicodeAttribute(null=True)

class DynamoDBRepository(IPromptRequestRepository):
    """DynamoDB implementation of result repository."""
    
    def get_prompt_request(self, request_id: RequestId) -> PromptRequest:
        """Get result from DynamoDB."""
        try:
            item = PromptRequestModel.get(request_id.value)
            return PromptRequest(
                request_id = RequestId(item.request_id),
                status = PromptStatus(item.status),
                result_url = ResultURL(item.result_url) if item.result_url else None
            )
        except PromptRequestModel.DoesNotExist:
            raise ValueError(f"Request {request_id.value} not found")