import json

from ..application.use_cases.process_prompt import ProcessPromptUseCase
from ..application.use_cases.save_result import SaveResultUseCase
from ..application.use_cases.update_status import UpdateStatusUseCase
from ..domain.entities import PromptRequest, PromptStatus, ProcessingResult
from ..domain.value_objects import RequestId, HumanPrompt, UserRoleArn, UserTables, AccountId
from ..infrastructure.llm.openai import OpenAIService
from ..infrastructure.storage.s3 import S3StorageService
from ..infrastructure.repository.dynamodb import DynamoDBRepository



# Initialize services and use cases
llm_service = OpenAIService()
storage_service = S3StorageService()
repository = DynamoDBRepository()

process_use_case = ProcessPromptUseCase(llm_service)
save_result_use_case = SaveResultUseCase(storage_service)
update_status_use_case = UpdateStatusUseCase(repository)

def handler(event, context):
    try:
        # Parse request
        body = json.loads(event['body'])
        
        # Create value objects
        request_id = RequestId(body['request_id'])
        human_prompt = HumanPrompt(body['prompt'])
        user_role_arn = UserRoleArn(body['user_role_arn'])
        account_id = AccountId(body['account_id'])
        user_tables = UserTables(body['tables'])
        status = PromptStatus(body['status'])
        created_at = body['created_at']


        prompt_request = PromptRequest(
            request_id=request_id,
            human_prompt=human_prompt,
            user_role_arn=user_role_arn,
            user_tables=user_tables,
            account_id=account_id,
            status=status,
            created_at=created_at
        )


        try:
            # 1. Process prompt
            processing_result: ProcessingResult = process_use_case.execute(prompt_request)
            
            # 2. Save result to S3
            result_url = save_result_use_case.execute(
                prompt_request.request_id, 
                processing_result 
            )
            
            # 3. Update status in DynamoDB
            update_status_use_case.execute(
                prompt_request.request_id,
                PromptStatus.COMPLETED,
                result_url
            )
            
            # Return success response
            return {
                'statusCode': 200
            }
            
        except Exception as e:
            # If any step fails, update status to FAILED
            update_status_use_case.execute(
                str(prompt_request.request_id.value),
                PromptStatus.FAILED
            )
            raise e
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        } 