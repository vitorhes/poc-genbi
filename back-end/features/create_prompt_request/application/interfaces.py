from abc import ABC, abstractmethod
from ..domain.entities import PromptRequest

class PromptRequestRepository(ABC):
    """
    Abstract repository interface for PromptRequest persistence operations.
    """
    @abstractmethod
    def save(self, prompt_request: PromptRequest) -> None:
        """
        Saves a PromptRequest to the persistence store.
        
        Args:
            prompt_request: The PromptRequest entity to save
            
        Raises:
            RepositoryError: If there's an error during save operation
        """
        pass 