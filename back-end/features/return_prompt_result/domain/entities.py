from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from .value_objects import RequestId, LLMResponse, ResultURL, HumanPrompt, UserRoleArn, UserTables, AccountId

class PromptStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

@dataclass(frozen=True)
class PromptRequest:
    """Domain entity representing a prompt request."""
    request_id: RequestId
    status: PromptStatus
    human_prompt: HumanPrompt | None = None
    user_role_arn: UserRoleArn | None = None
    user_tables: UserTables | None = None
    account_id: AccountId | None = None
    created_at: datetime | None = None
    result_url: ResultURL | None = None

@dataclass(frozen=True)
class PromptResult:
    """Result of prompt processing."""
    request_id:  RequestId
    llm_response: LLMResponse
    result_url: ResultURL 
    status: PromptStatus

