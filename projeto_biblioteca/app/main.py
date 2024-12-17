from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from database import engine
from fastapi import FastAPI
from handlers import author, book
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator


@asynccontextmanager
async def lifespan(app: FastAPI) -> "AsyncGenerator[None]":  # noqa: ARG001, RUF029
    SQLModel.metadata.drop_all(bind=engine, checkfirst=True)
    SQLModel.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=author.router, prefix="/autores", tags=["Authors"])
app.include_router(router=book.router, prefix="/livros", tags=["Books"])
