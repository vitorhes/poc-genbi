import boto3
from ...application.interfaces.storage import IStorageService
from ...domain.value_objects import RequestId, ResultContent
class S3StorageService(IStorageService):
    """S3 implementation of storage service."""
    
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket = "your-bucket-name"
        
    def save_result(self, request_id: RequestId, result_content: ResultContent) -> str:
        """Save result to S3 and return the URL."""
        key = f"results/{request_id.value}.json"
        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=result_content.value,
            ContentType='application/json'
        )
        return f"s3://{self.bucket}/{key}" 