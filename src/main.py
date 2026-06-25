from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.core.database import init_db
from src.presentation.api.routes.user_routes import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="MedScheduler", lifespan=lifespan)

app.include_router(user_router)


@app.get("/health")
def health():
    return {"status": "ok"}