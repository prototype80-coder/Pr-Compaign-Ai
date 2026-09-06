"""Application configuration, loaded from environment variables.

Centralizing config here means nothing else in the app reads os.environ
directly - services and routes depend on a typed Settings object instead,
which makes testing (override settings) and future changes (new env vars)
straightforward.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: str = "development"
    log_level: str = "info"

    database_url: str = "sqlite:///./pr_campaign_copilot.db"

    ai_provider: str = "cloudflare"
    cloudflare_account_id: str = ""
    cloudflare_api_token: str = ""
    cloudflare_ai_model: str = ""


@lru_cache
def get_settings() -> Settings:
    """Cached so we parse env vars once per process, not on every request."""
    return Settings()
