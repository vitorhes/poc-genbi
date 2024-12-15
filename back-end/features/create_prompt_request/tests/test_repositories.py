import pytest
from unittest.mock import patch, MagicMock
from ..infrastructure.repositories import DynamoDBPromptRequestRepository
from ..domain.entities import PromptRequest

class TestDynamoDBPromptRequestRepository:
    def test_save_prompt_request(self, valid_request_id, valid_human_prompt, valid_user_role_arn):
        with patch('features.create_prompt_request.infrastructure.repositories.PromptRequestModel') as MockModel:
            # Configure the mock
            mock_instance = MagicMock()
            MockModel.return_value = mock_instance

            repository = DynamoDBPromptRequestRepository()
            prompt_request = PromptRequest.create(
                request_id=valid_request_id,
                human_prompt=valid_human_prompt,
                user_role_arn=valid_user_role_arn
            )

            repository.save(prompt_request)

            # Verify the mock was called correctly
            MockModel.assert_called_once()
            
            # Get the actual call arguments
            call_args = MockModel.call_args[1]
            
            # Verify the required fields
            assert call_args['request_id'] == str(valid_request_id.value)
            assert call_args['human_prompt'] == valid_human_prompt.value
            assert call_args['status'] == prompt_request.status.value
            assert call_args['user_role_arn'] == valid_user_role_arn.value
            assert call_args['account_id'] == prompt_request.account_id.value
            assert 'created_at' in call_args
            assert call_args['result_url'] is None

            mock_instance.save.assert_called_once()