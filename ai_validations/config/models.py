from pydantic import BaseModel


class LLMConfig(BaseModel):
    model_name: str
    temperature: float
    max_tokens: int


class LoggingConfig(BaseModel):
    level: str


class FrameworkConfig(BaseModel):
    llm: LLMConfig
    logging: LoggingConfig