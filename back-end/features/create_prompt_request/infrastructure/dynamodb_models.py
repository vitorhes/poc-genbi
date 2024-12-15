from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute

class PromptRequestModel(Model):
    """
    DynamoDB model for storing prompt requests.
    """
    class Meta:
        table_name = "PromptRequests"
        region = "sa-east-1"

    request_id = UnicodeAttribute(hash_key=True)
    human_prompt = UnicodeAttribute()
    status = UnicodeAttribute()
    user_role_arn = UnicodeAttribute()
    account_id = UnicodeAttribute()
    created_at = UTCDateTimeAttribute()
    result_url = UnicodeAttribute(null=True)