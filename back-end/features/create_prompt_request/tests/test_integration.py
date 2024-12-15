import pytest
from datetime import datetime
from ..application.dto import CreatePromptRequestDTO
from ..application.use_cases import CreatePromptRequestUseCase
from ..infrastructure.repositories import DynamoDBPromptRequestRepository
from ..infrastructure.dynamodb_models import PromptRequestModel

class TestCreatePromptRequestIntegration:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        # Create the DynamoDB table if it doesn't exist
        if not PromptRequestModel.exists():
            PromptRequestModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        
        yield
        
        # Clean up after test
        for item in PromptRequestModel.scan():
        
            item.delete()

    def test_create_prompt_request_integration(self):
        # Arrange
        repository = DynamoDBPromptRequestRepository()
        use_case = CreatePromptRequestUseCase(repository)
        dto = CreatePromptRequestDTO(
            human_prompt="Test integration prompt",
            user_role_arn="arn:aws:iam::123456789012:role/test-role",
                        user_tables=[{"teste":"teste"}]
        )

        # Act
        request_id = use_case.execute(dto)

        # Assert
        # Fetch the created item from DynamoDB
        saved_items = list(PromptRequestModel.scan())
        assert len(saved_items) == 1
        
        saved_item = saved_items[0]
        assert saved_item.request_id == request_id
        assert saved_item.human_prompt == "Test integration prompt"
        assert saved_item.user_role_arn == "arn:aws:iam::123456789012:role/test-role"
        assert saved_item.status == "PENDING"
        assert isinstance(saved_item.created_at, datetime) 