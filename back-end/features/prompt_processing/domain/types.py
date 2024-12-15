from enum import Enum, auto

class PromptType(Enum):
    """Types of prompts that can be processed."""
    SQL_QUERY = auto()
    METADATA_ANALYSIS = auto()
    GENERAL = auto()

class ProcessingError(Exception):
    """Base error for prompt processing."""
    pass 