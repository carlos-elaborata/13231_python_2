from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class BaseModel(SQLModel):
    id_: int | None = Field(default=None, primary_key=True)


class AuthorBase(SQLModel):
    name: str = Field(index=True)


class BookBase(SQLModel):
    title: str = Field(index=True)
    genre: str
    isbn: str

    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, isbn: str) -> str:
        isbn = isbn.replace("-", "")

        if len(isbn) not in {10, 13}:
            msg = "O ISBN deve conter 10 ou 13 caracteres."
            raise ValueError(msg)

        return isbn


class Author(BaseModel, AuthorBase, table=True):
    link_book: list["AuthorBook"] = Relationship(
        back_populates="author",
        cascade_delete=True,
        sa_relationship_kwargs={"lazy": "select"},
    )


class Book(BaseModel, BookBase, table=True):
    link_author: list["AuthorBook"] = Relationship(
        back_populates="book",
        cascade_delete=True,
        sa_relationship_kwargs={"lazy": "select"},
    )


class AuthorBook(SQLModel, table=True):
    author_fk: int = Field(foreign_key="author.id_", primary_key=True)
    book_fk: int = Field(foreign_key="book.id_", primary_key=True)

    author: Author = Relationship(back_populates="link_book")
    book: Book = Relationship(back_populates="link_author")


# Modelos para operações CRUD


class AuthorCreate(AuthorBase):
    pass


class AuthorRead(BaseModel, AuthorBase):
    books: list[BookBase] = Field(default_factory=list)


class AuthorUpdate(SQLModel):
    name: str | None = None


class BookCreate(BookBase):
    pass


class BookRead(BaseModel, BookBase):
    authors: list[AuthorBase] = Field(default_factory=list)


class BookUpdate(SQLModel):
    title: str | None = None
    genre: str | None = None
    isbn: str | None = None


class AuthorBookCreate(SQLModel):
    author_fk: int
    book_fk: int


class AuthorBookRead(SQLModel):
    name: str
    title: str
