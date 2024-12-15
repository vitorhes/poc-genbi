from typing import Dict, Type
from ...domain.prompt import Prompt
from ...domain.types import PromptType
from ...application.interfaces.llm import LLMService
from .base import Agent
from .agents import SupervisorAgent, SQLAgent, AnalysisAgent, GeneralAgent

class AgentFactory:
    """Factory for creating appropriate agents."""
    
    def __init__(self, llm_service: LLMService):
        self.llm = llm_service
        
    def create_for_prompt(self, prompt: Prompt) -> Agent:
        """Create appropriate agent for the prompt."""
        # First, use supervisor agent to classify
        supervisor = self.create_supervisor()
        prompt_type = supervisor.classify(prompt)
        
        # Create appropriate agent based on classification
        if prompt_type == PromptType.SQL_QUERY:
            return SQLAgent(self.llm)
        elif prompt_type == PromptType.METADATA_ANALYSIS:
            return AnalysisAgent(self.llm)
        else:
            return GeneralAgent(self.llm)
            
    def create_supervisor(self) -> SupervisorAgent:
        """Create a supervisor agent."""
        return SupervisorAgent(self.llm)