from collections.abc import Generator
from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

if TYPE_CHECKING:
    from sqlalchemy import Engine

DATABASE_URI = "sqlite:///library.db"

connect_args: dict[str, bool] = {"check_same_thread": False}

engine: "Engine" = create_engine(
    url=DATABASE_URI,
    connect_args=connect_args,
    echo=False,
)


def get_session() -> Generator[Session]:
    with Session(bind=engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(dependency=get_session)]
