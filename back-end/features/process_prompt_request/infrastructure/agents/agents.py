from .base import Agent
from .prompts import PromptTemplates
from ...domain.value_objects import HumanPrompt
from ...domain.types import PromptType

class SupervisorAgent(Agent):
    """Agent responsible for classifying prompts."""
    
    def classify(self, human_prompt: HumanPrompt) -> PromptType:
        """Classify the prompt type."""
        classification = self.llm.complete(
            PromptTemplates.CLASSIFY.format(human_prompt=human_prompt.value)
        )
        
        if "SQL_QUERY" in classification:
            return PromptType.SQL_QUERY
        elif "METADATA_ANALYSIS" in classification:
            return PromptType.METADATA_ANALYSIS
        else:
            return PromptType.GENERAL
    
    def process(self, prompt: HumanPrompt) -> str:
        """Not used for supervisor agent."""
        raise NotImplementedError("Supervisor agent only classifies prompts")

    def _get_prompt_template(self) -> str:
        raise NotImplementedError("Supervisor agent only classifies prompts")

class SQLAgent(Agent):
    """Agent for SQL query generation."""
    
    def __init__(self, llm_service):
        super().__init__(llm_service)
        self.result_type = "sql_query"
    
    def _get_prompt_template(self) -> str:
        return PromptTemplates.SQL

class AnalysisAgent(Agent):
    """Agent for metadata analysis."""
    
    def __init__(self, llm_service):
        super().__init__(llm_service)
        self.result_type = "metadata_analysis"
    
    def _get_prompt_template(self) -> str:
        return PromptTemplates.ANALYSIS

class GeneralAgent(Agent):
    """Agent for general queries."""
    
    def __init__(self, llm_service):
        super().__init__(llm_service)
        self.result_type = "general"
    
    def _get_prompt_template(self) -> str:
        return PromptTemplates.GENERAL 