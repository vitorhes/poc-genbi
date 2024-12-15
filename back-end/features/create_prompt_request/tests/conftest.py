import pytest
from uuid import UUID
from ..domain.value_objects import RequestId, UserRoleArn, AccountId, HumanPrompt
from ..domain.entities import PromptRequest, PromptStatus
from ..infrastructure.repositories import DynamoDBPromptRequestRepository
from ..application.dto import CreatePromptRequestDTO

@pytest.fixture
def valid_request_id() -> RequestId:
    return RequestId(UUID('12345678-1234-5678-1234-567812345678'))

@pytest.fixture
def valid_user_role_arn() -> UserRoleArn:
    return UserRoleArn('arn:aws:iam::123456789012:role/test-role')

@pytest.fixture
def valid_account_id() -> AccountId:
    return AccountId('123456789012')

@pytest.fixture
def valid_human_prompt() -> HumanPrompt:
    return HumanPrompt('What is the weather today?')

@pytest.fixture
def valid_dto() -> CreatePromptRequestDTO:
    return CreatePromptRequestDTO(
        human_prompt='What is the weather today?',
        user_role_arn='arn:aws:iam::123456789012:role/test-role'
    )

@pytest.fixture
def mock_repository():
    class MockRepository:
        def __init__(self):
            self.save_called = False

        def save(self, prompt_request):
            self.save_called = True

    return MockRepository() 