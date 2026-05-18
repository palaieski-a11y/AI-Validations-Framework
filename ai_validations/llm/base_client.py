from abc import ABC, abstractmethod

from ai_validations.llm.models import (
    LLMRequest,
    LLMResponse
)


class BaseLLMClient(ABC):

    @abstractmethod
    def generate(
        self,
        request: LLMRequest
    ) -> LLMResponse:
        pass