import os

from openai import OpenAI

from ai_validations.llm.models import (
    LLMRequest,
    LLMResponse
)

from ai_validations.llm.base_client import BaseLLMClient


class OpenAIClient(BaseLLMClient):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate(
        self,
        request: LLMRequest
    ) -> LLMResponse:

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": request.prompt
                }
            ]
        )

        return LLMResponse(
            content=response.choices[0].message.content,
            model=response.model,
            tokens_used=response.usage.total_tokens
        )