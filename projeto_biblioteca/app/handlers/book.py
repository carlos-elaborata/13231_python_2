from database import SessionDep
from fastapi import APIRouter, HTTPException, status
from schemas import Book, BookCreate, BookUpdate
from sqlmodel import select

router = APIRouter()


@router.post(path="/")
def create_book(book: BookCreate, session: SessionDep) -> Book:
    validated_data: BookCreate = BookCreate.model_validate(obj=book)

    obj: Book = Book.model_validate(obj=validated_data)

    session.add(instance=obj)
    session.commit()
    session.refresh(instance=obj)

    return obj


@router.get(path="/{id_}")
def read_book(id_: int, session: SessionDep) -> Book:
    obj: Book | None = session.get(entity=Book, ident=id_)

    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado.",
        )

    return obj


@router.get(path="/")
def read_books(session: SessionDep) -> list[Book]:
    return list(session.exec(statement=select(Book)))


def update(
    id_: int,
    book: BookUpdate,
    session: SessionDep,
    partial: bool = False,
) -> Book:
    obj: Book | None = session.get(entity=Book, ident=id_)

    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado.",
        )

    validated_data: dict[str, str | int] = book.model_dump(exclude_unset=partial)
    for key, value in validated_data.items():
        setattr(obj, key, value)

    session.commit()
    session.refresh(instance=obj)

    return obj


@router.patch(path="/{id_}")
def patch_book(id_: int, book: BookUpdate, session: SessionDep) -> Book:
    return update(id_=id_, book=book, session=session, partial=True)


@router.put(path="/{id_}")
def put_book(id_: int, book: BookUpdate, session: SessionDep) -> Book:
    return update(id_=id_, book=book, session=session, partial=False)


@router.delete(path="/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id_: int, session: SessionDep) -> None:
    obj: Book | None = session.get(entity=Book, ident=id_)

    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado.",
        )

    session.delete(instance=obj)
    session.commit()
