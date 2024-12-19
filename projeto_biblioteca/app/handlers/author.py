from database import SessionDep
from fastapi import APIRouter, HTTPException, status
from schemas import (
    Author,
    AuthorCreate,
    AuthorPatch,
    AuthorPut,
    AuthorRead,
    AuthorReadWithBooks,
)
from sqlmodel import select

router = APIRouter(prefix="/autores", tags=["Authors"])


@router.post(path="/", status_code=status.HTTP_201_CREATED, response_model=AuthorRead)
def create_author(new_author: AuthorCreate, session: SessionDep) -> Author:
    author: Author = Author(**new_author.model_dump())
    session.add(instance=author)
    session.commit()
    session.refresh(instance=author)

    return author


@router.get(path="/{id_}", response_model=AuthorReadWithBooks)
def read_author(id_: int, session: SessionDep) -> Author:
    author: Author | None = session.get(entity=Author, ident=id_)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autor não encontrado.",
        )

    return author


@router.get(path="/")
def read_authors(session: SessionDep) -> list[Author]:
    return list(session.exec(statement=select(Author)))


@router.get(path="/livros/", response_model=list[AuthorReadWithBooks])
def read_authors_with_books(session: SessionDep) -> list[Author]:
    return list(session.exec(statement=select(Author)))


def update(
    id_: int,
    updated_author: AuthorPut | AuthorPatch,
    session: SessionDep,
    partial: bool = False,
) -> Author:
    author: Author | None = session.get(entity=Author, ident=id_)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autor não encontrado.",
        )

    updated_data: dict[str, str | int] = updated_author.model_dump(
        exclude_unset=partial,
    )
    for key, value in updated_data.items():
        setattr(author, key, value)

    session.commit()
    session.refresh(instance=author)

    return author


@router.patch(path="/{id_}", response_model=AuthorReadWithBooks)
def patch_author(id_: int, author: AuthorPatch, session: SessionDep) -> Author:
    return update(id_=id_, updated_author=author, session=session, partial=True)


@router.put(path="/{id_}", response_model=AuthorReadWithBooks)
def put_author(id_: int, author: AuthorPut, session: SessionDep) -> Author:
    return update(id_=id_, updated_author=author, session=session, partial=False)


@router.delete(path="/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(id_: int, session: SessionDep) -> None:
    author: Author | None = session.get(entity=Author, ident=id_)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autor não encontrado.",
        )

    session.delete(instance=author)
    session.commit()
