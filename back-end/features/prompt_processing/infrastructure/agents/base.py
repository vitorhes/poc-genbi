from abc import ABC, abstractmethod
from ...domain.prompt import Prompt
from ...application.interfaces.llm import LLMService

class Agent(ABC):
    """Base class for all agents."""
    
    def __init__(self, llm_service: LLMService):
        self.llm = llm_service
        self.result_type = "unknown"
    
    @abstractmethod
    def process(self, prompt: Prompt) -> str:
        """Process the prompt and return result."""
        pass 