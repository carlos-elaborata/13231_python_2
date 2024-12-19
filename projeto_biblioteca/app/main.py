from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from database import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from handlers.author import router as author_router
from handlers.book import router as book_router
from handlers.form import router as form_router
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator


@asynccontextmanager
async def lifespan(app: FastAPI) -> "AsyncGenerator[None]":  # noqa: ARG001, RUF029
    # SQLModel.metadata.drop_all(bind=engine, checkfirst=True)
    SQLModel.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

STATIC_DIR: Path = Path(__file__).parents[1] / "static"
app.mount(path="/static", app=StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(router=author_router)
app.include_router(router=book_router)
app.include_router(router=form_router)
