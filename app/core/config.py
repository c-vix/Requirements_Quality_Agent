from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

    database_url: str
    openai_api_key: str
    llm_model: str = "gpt-4o-mini"

    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    top_k: int = 3
    duplicate_threshold: float = 0.85
    related_threshold: float = 0.60

settings = Settings()