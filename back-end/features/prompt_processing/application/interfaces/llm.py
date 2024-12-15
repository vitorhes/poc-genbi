from typing import Protocol

class LLMService(Protocol):
    """Interface for LLM services."""
    
    def complete(self, prompt: str) -> str:
        """Get completion from LLM."""
        pass 