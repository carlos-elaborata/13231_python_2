from database import SessionDep
from fastapi import APIRouter, HTTPException, status
from schemas import Author, AuthorCreate, AuthorUpdate
from sqlmodel import select

router = APIRouter()


@router.post(path="/")
def create_author(author: AuthorCreate, session: SessionDep) -> Author:
    validated_data: AuthorCreate = AuthorCreate.model_validate(obj=author)

    obj: Author = Author.model_validate(obj=validated_data)

    session.add(instance=obj)
    session.commit()
    session.refresh(instance=obj)

    return obj


@router.get(path="/{id_}")
def read_author(id_: int, session: SessionDep) -> Author:
    obj: Author | None = session.get(entity=Author, ident=id_)

    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autor não encontrado.",
        )

    return obj


@router.get(path="/")
def read_authors(session: SessionDep) -> list[Author]:
    return list(session.exec(statement=select(Author)))


def update(
    id_: int,
    author: AuthorUpdate,
    session: SessionDep,
    partial: bool = False,
) -> Author:
    obj: Author | None = session.get(entity=Author, ident=id_)

    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autor não encontrado.",
        )

    validated_data: dict[str, str | int] = author.model_dump(exclude_unset=partial)
    for key, value in validated_data.items():
        setattr(obj, key, value)

    session.commit()
    session.refresh(instance=obj)

    return obj


@router.patch(path="/{id_}")
def patch_author(id_: int, author: AuthorUpdate, session: SessionDep) -> Author:
    return update(id_=id_, author=author, session=session, partial=True)


@router.put(path="/{id_}")
def put_author(id_: int, author: AuthorUpdate, session: SessionDep) -> Author:
    return update(id_=id_, author=author, session=session, partial=False)


@router.delete(path="/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(id_: int, session: SessionDep) -> None:
    obj: Author | None = session.get(entity=Author, ident=id_)

    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autor não encontrado.",
        )

    session.delete(instance=obj)
    session.commit()
