from uuid import uuid4
import logging
from dataclasses import dataclass
from .dto import CreatePromptRequestDTO
from .interfaces import PromptRequestRepository
from ..domain.entities import PromptRequest
from ..domain.value_objects import RequestId, UserRoleArn, HumanPrompt, UserTables

logger = logging.getLogger(__name__)

@dataclass
class CreatePromptRequestUseCase:
    """Use case for creating a new prompt request."""
    repository: PromptRequestRepository

    def execute(self, dto: CreatePromptRequestDTO) -> str:
        """Creates a new prompt request."""

        request_id = RequestId(uuid4())

        user_role_arn = UserRoleArn(dto.user_role_arn)
        human_prompt = HumanPrompt(dto.human_prompt)
        user_tables = UserTables(dto.user_tables)

        prompt_request = PromptRequest.create(
            request_id=request_id,
            human_prompt=human_prompt,
            user_role_arn=user_role_arn,
            user_tables=user_tables
        )

        logger.info(f"Creating prompt request with ID: {request_id.value}")
        self.repository.save(prompt_request)
        
        logger.info(f"Prompt request {request_id.value} saved successfully")

        return str(request_id.value)