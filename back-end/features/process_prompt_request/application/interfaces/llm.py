from typing import Protocol
from ...domain.value_objects import HumanPrompt
class ILLMService(Protocol):
    """Interface for LLM services."""
    
    def complete(self, human_prompt: HumanPrompt) -> str:
        """Get completion from LLM."""
        pass 