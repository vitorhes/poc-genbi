from typing import NamedTuple
from uuid import UUID
import re

class RequestId(NamedTuple):
    value: UUID

class AccountId(NamedTuple):
    value: str

    @classmethod
    def from_arn(cls, arn: str) -> "AccountId":
        """Extract AWS account ID from the ARN"""
        pattern = r'arn:aws:iam::(\d+):role/'
        match = re.match(pattern, arn)
        if not match:
            raise ValueError(f"Invalid ARN format: {arn}")
        return cls(match.group(1))

class UserRoleArn(NamedTuple):
    value: str

class HumanPrompt(NamedTuple):
    value: str
