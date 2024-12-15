
from ...domain.types import PromptType
from ...application.interfaces.llm import ILLMService
from .base import Agent
from .agents import SupervisorAgent, SQLAgent, AnalysisAgent, GeneralAgent

class AgentFactory:
    """Factory for creating appropriate agents."""
    
    def __init__(self, llm_service: ILLMService):
        self.llm = llm_service
        self._agent_map = {
            PromptType.SQL_QUERY: SQLAgent,
            PromptType.METADATA_ANALYSIS: AnalysisAgent,
            PromptType.GENERAL: GeneralAgent
        }
        
    def create_supervisor(self) -> SupervisorAgent:
        """Create a supervisor agent."""
        return SupervisorAgent(self.llm)
            
    def create_agent_by_type(self, prompt_type: PromptType) -> Agent:
        """Create an agent based on type."""
        agent_class = self._agent_map.get(prompt_type, GeneralAgent)
        return agent_class(self.llm)