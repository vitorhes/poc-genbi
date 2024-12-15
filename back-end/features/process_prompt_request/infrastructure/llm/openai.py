import os
from openai import OpenAI
from ...application.interfaces.llm import ILLMService
from ...domain.types import ProcessingError
from ...domain.value_objects import HumanPrompt

class OpenAIService(ILLMService):
    """OpenAI implementation of LLM service."""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.model = "gpt-4-1106-preview"
        
    def complete(self, human_prompt: HumanPrompt) -> str:
        """Get completion from OpenAI."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": human_prompt.value}],
                temperature=0
            )
            return response.choices[0].message.content
        except Exception as e:
            raise ProcessingError(f"OpenAI API error: {str(e)}") 