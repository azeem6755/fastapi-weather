import pytz
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi.templating import Jinja2Templates


class Settings(BaseSettings):
    APP_NAME: str = "Weather APP"
    ENV: str
    api_base_url: str
    weather_api_key: str
    redis_host: str
    redis_port: int
    debug: bool = True

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()

templates = Jinja2Templates(directory='templates')

timezone = pytz.timezone("Asia/Kolkata")