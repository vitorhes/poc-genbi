class PromptTemplates:
    """Collection of prompt templates."""
    
    CLASSIFY = """Analyze this prompt and classify as either:
    - SQL_QUERY: For data querying/analysis needing SQL
    - METADATA_ANALYSIS: For questions about data structure/relationships
    - GENERAL: For other questions
    
    Prompt: {text}
    
    Respond with only the classification.
    """
    
    SQL = """Given these tables:
    {table_info}
    
    Convert this to SQL:
    {text}
    
    Return only the SQL query.
    """
    
    ANALYSIS = """Given these tables:
    {table_info}
    
    Analyze this request:
    {text}
    
    Focus on data relationships and structure.
    """
    
    GENERAL = """Given these tables:
    {table_info}
    
    Help with this request:
    {text}
    
    Provide a clear, focused response.
    """ 