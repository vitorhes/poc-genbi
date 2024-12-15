from abc import ABC, abstractmethod
from ...domain.value_objects import HumanPrompt, UserTables
from ...application.interfaces.llm import ILLMService

class Agent(ABC):
    """Base class for all agents."""
    
    def __init__(self, llm_service: ILLMService):
        self.llm = llm_service
        self.result_type = "unknown"
    
    def process(self, human_prompt: HumanPrompt, user_tables: UserTables) -> str:
        """Template method for processing prompts."""
    
        return self.llm.complete(
            self._get_prompt_template().format(
                human_prompt=human_prompt,
                user_tables=user_tables
            )
        )

    @abstractmethod
    def _get_prompt_template(self) -> str:
        """Get the prompt template for this agent."""
        pass
