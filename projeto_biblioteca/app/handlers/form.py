from pathlib import Path
from typing import TYPE_CHECKING

from database import SessionDep
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from schemas import Author
from sqlmodel import select
from starlette.templating import _TemplateResponse

if TYPE_CHECKING:
    from collections.abc import Sequence

router = APIRouter()


TEMPLATES_DIR: Path = Path(__file__).parents[2] / "templates"

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/lista-autores")
def get_author_form(request: Request, session: SessionDep) -> _TemplateResponse:
    authors: Sequence[Author] = session.exec(statement=select(Author)).all()

    return templates.TemplateResponse(
        request=request,
        name="generate_author_books.html",
        context={"authors": authors, "selected_author": None, "list_books": []},
    )
