import os

from dotenv import load_dotenv

from ai_validations.config.models import (
    LLMConfig,
    LoggingConfig,
    FrameworkConfig
)

load_dotenv()


def load_config() -> FrameworkConfig:

    llm_config = LLMConfig(
        model_name=os.getenv("DEFAULT_MODEL"),
        temperature=float(os.getenv("TEMPERATURE")),
        max_tokens=int(os.getenv("MAX_TOKENS"))
    )

    logging_config = LoggingConfig(
        level=os.getenv("LOG_LEVEL")
    )

    return FrameworkConfig(
        llm=llm_config,
        logging=logging_config
    )