from dataclasses import dataclass
from enum import Enum
from datetime import datetime, UTC
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
    account_id: AccountId
    user_tables: UserTables
    status: PromptStatus
    created_at: datetime
    result_url: str | None = None

    @classmethod
    def create(cls, request_id: RequestId, human_prompt: HumanPrompt, user_role_arn: UserRoleArn, user_tables: UserTables) -> "PromptRequest":
        """Factory to create PromptRequests"""
        account_id = AccountId.from_arn(user_role_arn.value)
        return cls(
            request_id=request_id,
            human_prompt=human_prompt,
            user_role_arn=user_role_arn,
            account_id=account_id,
            user_tables=user_tables,
            status=PromptStatus.PENDING,
            created_at=datetime.now(UTC)
        )