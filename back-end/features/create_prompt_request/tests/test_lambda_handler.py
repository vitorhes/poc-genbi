import pytest
import json
from unittest.mock import patch
from ..presentation.lambda_handler import lambda_handler

class TestLambdaHandler:
    @patch('features.create_prompt_request.presentation.lambda_handler.use_case')
    def test_lambda_handler_success(self, mock_use_case):
        mock_use_case.execute.return_value = "test-id"
        event = {
            'body': json.dumps({
                'human_prompt': 'What is the weather?',
                'user_role_arn': 'arn:aws:iam::123456789012:role/test-role'
            })
        }

        response = lambda_handler(event, None)
        
        assert response['statusCode'] == 201
        assert json.loads(response['body'])['request_id'] == "test-id"

    def test_lambda_handler_missing_prompt(self):
        event = {
            'body': json.dumps({
                'user_role_arn': 'arn:aws:iam::123456789012:role/test-role'
            })
        }

        response = lambda_handler(event, None)
        
        assert response['statusCode'] == 400
        assert 'error' in json.loads(response['body'])

    def test_lambda_handler_missing_role_arn(self):
        event = {
            'body': json.dumps({
                'human_prompt': 'What is the weather?'
            })
        }

        response = lambda_handler(event, None)
        
        assert response['statusCode'] == 400
        assert 'error' in json.loads(response['body'])

    def test_lambda_handler_invalid_json(self):
        event = {
            'body': 'invalid json'
        }

        response = lambda_handler(event, None)
        
        assert response['statusCode'] == 500
        assert 'error' in json.loads(response['body']) 