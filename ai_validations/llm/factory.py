from ai_validations.llm.openai_client import OpenAIClient


class LLMFactory:

    @staticmethod
    def create(provider: str):

        if provider == "openai":
            return OpenAIClient()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )