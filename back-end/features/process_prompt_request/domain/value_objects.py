from typing import NamedTuple, List
from uuid import UUID

class RequestId(NamedTuple):
    value: UUID

class UserRoleArn(NamedTuple):
    value: str

class HumanPrompt(NamedTuple):
    value: str

class UserTables(NamedTuple):
    value: List[dict]

class AccountId(NamedTuple):
    value: str

class ResultURL(NamedTuple):
    value: str

class ResultContent(NamedTuple):
    value: str