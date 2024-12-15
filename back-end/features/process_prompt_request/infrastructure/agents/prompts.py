class PromptTemplates:
    """Collection of prompt templates."""
    
    CLASSIFY = """Analyze this prompt and classify as either:
    - SQL_QUERY: For data querying/analysis needing SQL
    - METADATA_ANALYSIS: For questions about data structure/relationships
    - GENERAL: For other questions
    
    Prompt: {human_prompt}
    
    Respond with only the classification.
    """
    
    SQL = """Given these tables:
    {user_tables}
    
    Convert this to SQL:
    {human_prompt}
    
    Return only the SQL query.
    """
    
    ANALYSIS = """Given these tables:
    {user_tables}
    
    Analyze this request:
    {human_prompt}
    
    Focus on data relationships and structure.
    """
    
    GENERAL = """Given these tables:
    {user_tables}
    
    Help with this request:
    {human_prompt}
    
    Provide a clear, focused response.
    """ 