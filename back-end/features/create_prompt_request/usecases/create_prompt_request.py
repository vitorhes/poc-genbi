import uuid
import logging
from ..domain.prompt_request import PromptRequest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PromptRequestDTO:
    def __init__(self, human_prompt: str, user_id: str):
        self.human_prompt = human_prompt
        self.user_id = user_id

def create_prompt_request(dto: PromptRequestDTO) -> str:
    """
    Creates a new prompt request and saves it to the database.

    Args:
        dto (PromptRequestDTO): Data transfer object containing the human prompt and user ID.

    Returns:
        str: The unique request ID for the created prompt request.
    """
    request_id = str(uuid.uuid4())
    logger.info(f"Creating prompt request with ID: {request_id}")

    prompt_request = PromptRequest(
        request_id=request_id,
        human_prompt=dto.human_prompt,
        status="PENDING",
        user_id=dto.user_id
    )
    prompt_request.save()
    logger.info(f"Prompt request with ID: {request_id} saved successfully")

    return request_id 