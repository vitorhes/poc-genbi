import json
from typing import Any, Dict
from ..application.dto import CreatePromptRequestDTO
from ..application.use_cases import CreatePromptRequestUseCase
from ..infrastructure.repositories import DynamoDBPromptRequestRepository

repository = DynamoDBPromptRequestRepository()
use_case = CreatePromptRequestUseCase(repository)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    
    try:
        body = json.loads(event['body'])
        human_prompt = body.get('human_prompt')
        user_role_arn = body.get('user_role_arn')
        user_tables = body.get('user_tables')
        if not human_prompt or not user_role_arn:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Prompt and user role ARN are required'})
            }

        dto = CreatePromptRequestDTO(
            human_prompt=human_prompt,
            user_role_arn=user_role_arn,
            user_tables=user_tables
        )
        
        request_id = use_case.execute(dto)

        return {
            'statusCode': 201,
            'body': json.dumps({'request_id': request_id})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        } 