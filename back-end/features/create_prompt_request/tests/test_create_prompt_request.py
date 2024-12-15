import pytest
from datetime import datetime, UTC
from ..application.dto import CreatePromptRequestDTO
from ..application.use_cases import CreatePromptRequestUseCase
from ..domain.entities import PromptRequest, PromptStatus
from ..domain.value_objects import RequestId, UserRoleArn, HumanPrompt

def test_create_prompt_request(mock_repository):
    human_prompt = "What is the weather today?"
    user_role_arn = "arn:aws:iam::123456789012:role/test-role"
    
    dto = CreatePromptRequestDTO(human_prompt=human_prompt, user_role_arn=user_role_arn)
    use_case = CreatePromptRequestUseCase(repository=mock_repository)
    request_id = use_case.execute(dto)
    
    assert request_id is not None
    assert mock_repository.save_called
    
def test_prompt_request_entity():
    request_id = RequestId("123")
    human_prompt = HumanPrompt("Test prompt")
    user_role_arn = UserRoleArn("arn:aws:iam::123456789012:role/test-role")
    
    prompt_request = PromptRequest.create(
        request_id=request_id,
        human_prompt=human_prompt,
        user_role_arn=user_role_arn
    )
    
    assert prompt_request.request_id == request_id
    assert prompt_request.human_prompt == human_prompt
    assert prompt_request.status == PromptStatus.PENDING
    assert prompt_request.user_role_arn == user_role_arn
    assert isinstance(prompt_request.created_at, datetime) 