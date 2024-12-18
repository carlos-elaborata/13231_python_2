from database import SessionDep
from fastapi import APIRouter, HTTPException, status
from schemas import Author, Book, BookCreate, BookPatch, BookPut, BookReadWithAuthors
from sqlmodel import select

router = APIRouter()


def get_authors_by_ids(
    authors_ids: list[int],
    session: SessionDep,
) -> list[Author] | None:
    authors = list(
        session.exec(statement=select(Author).where(Author.id_.in_(authors_ids))).all(),  # type: ignore[reportAttributeAccessIssue]
    )

    if len(authors) != len(authors_ids):
        return None

    return authors


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=BookReadWithAuthors,
)
def create_book(new_book: BookCreate, session: SessionDep) -> Book:
    authors: list[Author] | None = get_authors_by_ids(
        authors_ids=new_book.authors_ids,
        session=session,
    )

    if not authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Um ou mais autores não encontrados.",
        )

    book: Book = Book(**new_book.model_dump(exclude={"authors_ids"}))

    book.authors = authors

    session.add(instance=book)
    session.commit()
    session.refresh(instance=book)

    return book


@router.get(path="/{id_}", response_model=BookReadWithAuthors)
def read_book(id_: int, session: SessionDep) -> Book:
    book: Book | None = session.get(entity=Book, ident=id_)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado.",
        )

    return book


@router.get(path="/", response_model=list[BookReadWithAuthors])
def read_books(session: SessionDep) -> list[Book]:
    return list(session.exec(statement=select(Book)))


@router.patch(path="/{id_}", response_model=BookReadWithAuthors)
def patch_book(id_: int, updated_book: BookPatch, session: SessionDep) -> Book:
    book: Book | None = session.get(entity=Book, ident=id_)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado.",
        )

    updated_data: dict = updated_book.model_dump(
        exclude_unset=True,
    )

    if "authors_ids" in updated_data:
        authors_ids: list[int] = updated_data.pop("authors_ids")

        authors: list[Author] | None = get_authors_by_ids(
            authors_ids=authors_ids,
            session=session,
        )

        if not authors:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Um ou mais autores não encontrados.",
            )

        book.authors = authors

    for key, value in updated_data.items():
        setattr(book, key, value)

    session.add(instance=book)
    session.commit()
    session.refresh(instance=book)

    return book


@router.put(path="/{id_}", response_model=BookReadWithAuthors)
def put_book(id_: int, updated_book: BookPut, session: SessionDep) -> Book:
    authors: list[Author] | None = get_authors_by_ids(
        authors_ids=updated_book.authors_ids,
        session=session,
    )

    if not authors:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Um ou mais autores não encontrados.",
        )

    book: Book | None = session.get(entity=Book, ident=id_)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado.",
        )

    updated_data: dict[str, str | int] = updated_book.model_dump(
        exclude_unset=False,
        exclude={"authors_ids"},
    )
    for key, value in updated_data.items():
        setattr(book, key, value)

    book.authors = authors

    session.add(instance=book)
    session.commit()
    session.refresh(instance=book)

    return book


@router.delete(path="/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id_: int, session: SessionDep) -> None:
    book: Book | None = session.get(entity=Book, ident=id_)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado.",
        )

    session.delete(instance=book)
    session.commit()
