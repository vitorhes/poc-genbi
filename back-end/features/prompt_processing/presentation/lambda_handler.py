import json
from uuid import UUID
from ..application.process_prompt import ProcessPromptUseCase
from ..domain.prompt import Prompt, TableMetadata, ColumnMetadata
from ..infrastructure.llm.openai import OpenAIService

        # Process prompt
llm_service = OpenAIService()
use_case = ProcessPromptUseCase(llm_service)


def handler(event, context):
    try:
        # Parse request
        body = json.loads(event['body'])
        
        # Create prompt from request
        human_prompt = Prompt(
            id=UUID(body['request_id']),
            text=body['prompt'],
            tables=[
                TableMetadata(
                    name=t['name'],
                    columns=[
                        ColumnMetadata(name=c['name'], description=c['description'])
                        for c in t['columns']
                    ]
                )
                for t in body['tables']
            ],
            user_role_arn=body['user_role_arn']
        )

        result = use_case.execute(human_prompt)

        
        # Return response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'request_id': str(result.prompt_id),
                'result': result.content,
                'type': result.type
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        } 