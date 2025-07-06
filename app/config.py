from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    github_token: str
    fallback_mode: str = "smart"
    grace_days: int = 2
    log_level: str = "info"
    default_commit_message: str = "Updated content with GitAutoPush"


    class Config:
        env_file = ".env"


settings=Settings()


#to use this config in other file just do
#from app.config import settings

#token = settings.github_token
#mode = settings.fallback_mode