from pydantic import BaseModel


class LLMRequest(BaseModel):
    prompt: str


class LLMResponse(BaseModel):
    content: str
    model: str
    tokens_used: int