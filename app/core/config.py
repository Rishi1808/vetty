from pydantic import BaseSettings

class Settings(BaseSettings):
    API_KEY: str
    COINGECKO_API_URL: str = "https://api.coingecko.com/api/v3"

    class Config:
        env_file = ".env"

settings = Settings()