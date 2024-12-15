from .base import Agent
from .prompts import PromptTemplates
from ...domain.prompt import Prompt
from ...domain.types import PromptType

class SupervisorAgent(Agent):
    """Agent responsible for classifying prompts."""
    
    def classify(self, prompt: Prompt) -> PromptType:
        """Classify the prompt type."""
        classification = self.llm.complete(
            PromptTemplates.CLASSIFY.format(text=prompt.text)
        )
        
        if "SQL_QUERY" in classification:
            return PromptType.SQL_QUERY
        elif "METADATA_ANALYSIS" in classification:
            return PromptType.METADATA_ANALYSIS
        else:
            return PromptType.GENERAL
    
    def process(self, prompt: Prompt) -> str:
        """Not used for supervisor agent."""
        raise NotImplementedError("Supervisor agent only classifies prompts")

class SQLAgent(Agent):
    """Agent for SQL query generation."""
    
    def __init__(self, llm_service):
        super().__init__(llm_service)
        self.result_type = "sql_query"
    
    def process(self, prompt: Prompt) -> str:
        table_info = self._format_table_info(prompt.tables)
        return self.llm.complete(
            PromptTemplates.SQL.format(
                text=prompt.text,
                table_info=table_info
            )
        )

class AnalysisAgent(Agent):
    """Agent for metadata analysis."""
    
    def __init__(self, llm_service):
        super().__init__(llm_service)
        self.result_type = "metadata_analysis"
    
    def process(self, prompt: Prompt) -> str:
        table_info = self._format_table_info(prompt.tables)
        return self.llm.complete(
            PromptTemplates.ANALYSIS.format(
                text=prompt.text,
                table_info=table_info
            )
        )

class GeneralAgent(Agent):
    """Agent for general queries."""
    
    def __init__(self, llm_service):
        super().__init__(llm_service)
        self.result_type = "general"
    
    def process(self, prompt: Prompt) -> str:
        table_info = self._format_table_info(prompt.tables)
        return self.llm.complete(
            PromptTemplates.GENERAL.format(
                text=prompt.text,
                table_info=table_info
            )
        ) 