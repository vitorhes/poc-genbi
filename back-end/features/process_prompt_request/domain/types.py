from enum import Enum

class PromptType(Enum):
    """Types of prompts that can be processed."""
    SQL_QUERY = "sql_query"
    METADATA_ANALYSIS = "metadata_analysis"
    GENERAL = "general"

class ProcessingError(Exception):
    """Base error for prompt processing."""
    pass 