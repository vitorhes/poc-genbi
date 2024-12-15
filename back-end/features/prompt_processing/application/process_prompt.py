from dataclasses import dataclass
from ..domain.prompt import Prompt, ProcessingResult
from ..domain.types import ProcessingError
from .interfaces.llm import LLMService
from ..infrastructure.agents.factory import AgentFactory

@dataclass
class ProcessPromptUseCase:
    """Main use case for processing prompts."""
    
    llm_service: LLMService

    def execute(self, prompt: Prompt) -> ProcessingResult:
        """
        Process a prompt and return the result.
        
        Args:
            prompt: The prompt to process
            
        Returns:
            ProcessingResult: The processing result
            
        Raises:
            ProcessingError: If processing fails
        """
        try:
            # Create agent factory
            factory = AgentFactory(self.llm_service)
            
            # Get appropriate agent and process
            agent = factory.create_for_prompt(prompt)
            result = agent.process(prompt)
            
            return ProcessingResult(
                prompt_id=prompt.id,
                content=result,
                type=agent.result_type
            )
            
        except Exception as e:
            raise ProcessingError(f"Failed to process prompt: {str(e)}") 