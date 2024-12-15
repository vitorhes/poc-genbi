from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from .value_objects import RequestId, UserRoleArn, AccountId, HumanPrompt, UserTables

class PromptStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

@dataclass(frozen=True)
class PromptRequest:
    """Domain entity representing a prompt request."""
    request_id: RequestId
    human_prompt: HumanPrompt
    user_role_arn: UserRoleArn
    user_tables: UserTables
    account_id: AccountId
    status: PromptStatus
    created_at: datetime
    result_url: str | None = None

@dataclass(frozen=True)
class ProcessingResult:
    """Result of prompt processing."""
    result: str