from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass(frozen=True)
class ColumnMetadata:
    """Column metadata information."""
    name: str
    description: str

@dataclass(frozen=True)
class TableMetadata:
    """Table metadata information."""
    name: str
    columns: List[ColumnMetadata]

@dataclass(frozen=True)
class Prompt:
    """User prompt with context."""
    id: UUID
    text: str
    tables: List[TableMetadata]
    user_role_arn: str

@dataclass(frozen=True)
class ProcessingResult:
    """Result of prompt processing."""
    prompt_id: UUID
    content: str
    type: str  # Could be 'sql_query', 'analysis', etc. 