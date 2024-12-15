from typing import NamedTuple

class CreatePromptRequestDTO(NamedTuple):
    human_prompt: str
    user_role_arn: str