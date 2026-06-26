from pydantic import BaseModel
import os


class Settings(BaseModel):
    DB_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DATABASE_PORT", 5432))
    DB_NAME: str = os.getenv("DATABASE_NAME", "medscheduler")
    DB_USER: str = os.getenv("DATABASE_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "postgres")


settings = Settings()