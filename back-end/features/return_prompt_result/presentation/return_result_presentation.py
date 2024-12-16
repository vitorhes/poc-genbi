# back-end/features/return_prompt_result/presentation/return_result_presentation.py
import json
from ..application.use_cases.get_result import GetResultUseCase
from ..domain.entities import PromptResult, PromptStatus
from ..domain.value_objects import RequestId
from ..infrastructure.repository.dynamodb import DynamoDBRepository
from ..infrastructure.storage.s3 import S3StorageService


    
use_case = GetResultUseCase(
            repository = DynamoDBRepository(),
            storage_service = S3StorageService()
        )

def handler(event, context):
    """Lambda handler for returning prompt results."""
    try:
     
        request_id = RequestId(event['request_id'])
        
        # Execute use case
        result: PromptResult = use_case.execute(request_id)
        
        # Return response based on status
        if result.status == PromptStatus.COMPLETED:
            return {
                'statusCode': 200,
                'body': result.content.value,
                'headers': {
                    'Content-Type': 'text/plain'
                }
            }
        elif result.status == PromptStatus.FAILED:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Processing failed'})
            }
        else:
            return {
                'statusCode': 202,
                'body': json.dumps({
                    'status': result.status.value,
                    'message': 'Processing not completed'
                })
            }
            
    except ValueError as e:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }