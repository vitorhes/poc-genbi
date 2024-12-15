from dataclasses import dataclass
from ...domain.types import ProcessingError
from ...domain.entities import PromptRequest, ProcessingResult
from ..interfaces.llm import ILLMService
from ...infrastructure.agents.factory import AgentFactory

@dataclass
class ProcessPromptUseCase:
    """Main use case for processing prompts."""
    
    llm_service: ILLMService

    def execute(self, prompt_request: PromptRequest) -> ProcessingResult:
        """
        Process Prompt Request and return the result.
        
        Args:
            prompt: The prompt to process
            
        Returns:
            ProcessingResult: The processing result
            
        Raises:
            ProcessingError: If processing fails
        """
        try:
            human_prompt = prompt_request.human_prompt
            factory = AgentFactory(self.llm_service)
            
            # First, use supervisor to classify
            supervisor = factory.create_supervisor()
            prompt_type = supervisor.classify(human_prompt)
            
            # Then create and use appropriate agent
            agent = factory.create_agent_by_type(prompt_type)
            result = agent.process(human_prompt)
            
            return ProcessingResult(
                result=result
            )
            
        except Exception as e:
            raise ProcessingError(f"Failed to process prompt: {str(e)}") 