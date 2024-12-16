import boto3
import json
from ...domain.value_objects import ResultContent, ResultURL
from ...application.interfaces.storage import IStorageService

class S3StorageService(IStorageService):
    """S3 implementation of storage service."""
    
    def __init__(self):
        self.s3 = boto3.client('s3')
    
    def get_result(self, url: ResultURL) -> ResultContent:
        """Get result from S3."""
        # Parse S3 URL
        bucket = url.split('/')[2]
        key = '/'.join(url.split('/')[3:])
        
        try:
            response = self.s3.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8')
            return ResultContent(content)
        except Exception as e:
            raise ValueError(f"Failed to get result from S3: {str(e)}")