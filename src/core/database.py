from sqlmodel import create_engine, Session, SQLModel
from src.infrastructure.database.models.user_model import UserModel

from src.core.config import settings

DATABASE_URL = (
    f"postgresql+psycopg2://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@{settings.DB_HOST}:"
    f"{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
        
def init_db():
    SQLModel.metadata.create_all(engine)