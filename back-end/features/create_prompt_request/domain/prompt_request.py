from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class PromptRequest(Model):
    class Meta:
        table_name = "PromptRequests"
        region = "us-west-2"  # Ensure this is set to your AWS region

    request_id = UnicodeAttribute(hash_key=True)
    human_prompt = UnicodeAttribute()
    status = UnicodeAttribute(default="PENDING")
    result_url = UnicodeAttribute(null=True)
    user_id = UnicodeAttribute() 