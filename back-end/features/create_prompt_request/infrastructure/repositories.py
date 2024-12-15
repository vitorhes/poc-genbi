from ..application.interfaces import PromptRequestRepository
from ..domain.entities import PromptRequest
from .dynamodb_models import PromptRequestModel

class DynamoDBPromptRequestRepository(PromptRequestRepository):
    """
    DynamoDB implementation of the PromptRequestRepository.
    """
    def save(self, prompt_request: PromptRequest) -> None:
        """
        Saves a PromptRequest to DynamoDB.
        """
        model = PromptRequestModel(
            request_id=str(prompt_request.request_id.value),
            human_prompt=prompt_request.human_prompt.value,
            status=prompt_request.status.value,
            user_role_arn=prompt_request.user_role_arn.value,
            account_id=prompt_request.account_id.value,
            created_at=prompt_request.created_at,
            result_url=prompt_request.result_url
        )
        model.save()