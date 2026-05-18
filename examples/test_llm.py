from ai_validations.llm.factory import LLMFactory

from ai_validations.llm.models import LLMRequest


client = LLMFactory.create("openai")

response = client.generate(
    LLMRequest(
        prompt="Explain AI testing in one sentence."
    )
)

print(response)
