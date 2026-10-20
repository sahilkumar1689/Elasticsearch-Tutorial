# app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ELASTIC_URL: str
    ELASTIC_API_KEY: str
    PRODUCT_INDEX: str = "products"

    class Config:
        env_file = ".env"

settings = Settings()
