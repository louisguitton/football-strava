from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    strava_client_id: str
    strava_client_secret: str

    class Config:
        env_file = ".env"


@lru_cache()
def generate_settings() -> Settings:
    return Settings()
