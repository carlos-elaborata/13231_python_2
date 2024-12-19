from collections.abc import Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Annotated

import httpx
import pandas as pd
from database import SessionDep
from fastapi import APIRouter, Form, HTTPException, Request, status
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from schemas import Author, AuthorBook, Book
from sqlmodel import select
from starlette.templating import _TemplateResponse

if TYPE_CHECKING:
    from collections.abc import Sequence

router = APIRouter(include_in_schema=False)


TEMPLATES_DIR: Path = Path(__file__).parents[2] / "templates"
TEMP_DIR: Path = Path(__file__).parents[2] / "temp"

templates = Jinja2Templates(directory=TEMPLATES_DIR)


def get_book_infos(isbn: str) -> dict[str, str]:
    url: str = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"

    resposta: httpx.Response = httpx.get(url=url, timeout=10)

    url_google_books: str = ""
    url_cover: str = ""

    if resposta.is_success:
        data: dict = resposta.json()

        if data["totalItems"] > 0:
            for item in data["items"]:
                url_google_books = item["volumeInfo"].get("canonicalVolumeLink", "")

                url_cover = (
                    item["volumeInfo"].get("imageLinks", {}).get("thumbnail", "")
                )

                if url_cover:
                    return {
                        "url_cover": url_cover,
                        "url_google_books": url_google_books,
                    }
    return {
        "url_cover": url_cover,
        "url_google_books": url_google_books,
    }


@router.get(path="/lista-autores")
def get_author_form(request: Request, session: SessionDep) -> _TemplateResponse:
    authors: Sequence[Author] = session.exec(statement=select(Author)).all()

    return templates.TemplateResponse(
        request=request,
        name="generate_author_books.html",
        context={"authors": authors, "selected_author": None, "list_books": []},
    )


@router.post(path="/lista-autores")
def generate_author_books_html(
    request: Request,
    session: SessionDep,
    id_: Annotated[int | None, Form(default=...)] = None,
) -> _TemplateResponse:
    authors: Sequence[Author] = session.exec(statement=select(Author)).all()

    selected_author = None
    list_books: list[dict[str, Book | str | None]] = []

    if id_:
        selected_author: Author | None = session.get(entity=Author, ident=id_)

        if selected_author:
            books: Sequence[Book] = session.exec(
                statement=select(Book)
                .join(target=AuthorBook)
                .where(AuthorBook.author_fk == id_),
            ).all()

            for book in books:
                url_data: dict[str, str] = get_book_infos(isbn=book.isbn)

                list_books.append({
                    "book": book,
                    "url_cover": url_data["url_cover"],
                    "url_google_books": url_data["url_google_books"],
                })

    return templates.TemplateResponse(
        request=request,
        name="generate_author_books.html",
        context={
            "authors": authors,
            "selected_author": selected_author,
            "list_books": list_books,
        },
    )


@router.post(path="/gerar-excel")
def generate_excel(
    id_: Annotated[int, Form(default=...)],
    session: SessionDep,
) -> FileResponse:
    author: Author | None = session.get(entity=Author, ident=id_)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autor não encontrado.",
        )

    books: Sequence[Book] = session.exec(
        statement=select(Book)
        .join(target=AuthorBook)
        .where(AuthorBook.author_fk == id_),
    ).all()

    books_data: list[dict[str, str]] = [
        {
            "Título": book.title,
            "Gênero": book.genre,
            "ISBN": book.isbn,
        }
        for book in books
    ]

    df_books = pd.DataFrame(data=books_data)

    filename: str = f"{author.name.replace(' ', '_')}_books.xlsx"

    filepath: Path = TEMP_DIR / filename

    df_books.to_excel(excel_writer=filepath, index=False)

    return FileResponse(path=filepath, filename=filename)
