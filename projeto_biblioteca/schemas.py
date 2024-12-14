from sqlmodel import Field, Relationship, SQLModel


class AuthorBase(SQLModel):
    name: str = Field(index=True)


class Author(AuthorBase, table=True):
    id_: int | None = Field(default=None, primary_key=True)

    link_book: list["AuthorBook"] = Relationship(back_populates="author")


class AuthorCreate(AuthorBase):
    pass


class AuthorRead(AuthorBase):
    id_: int
    books: list["Book"] = []


class AuthorUpdate(SQLModel):
    name: str | None = None


class BookBase(SQLModel):
    title: str = Field(index=True)
    genre: str
    isbn: str


class Book(BookBase, table=True):
    id_: int | None = Field(default=None, primary_key=True)

    link_author: list["AuthorBook"] = Relationship(back_populates="book")


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id_: int
    authors: list[Author] = []


class BookUpdate(SQLModel):
    title: str | None = None
    genre: str | None = None
    isbn: str | None = None


class AuthorBookBase(SQLModel):
    author_fk: int
    book_fk: int


class AuthorBook(SQLModel, table=True):
    author_fk: int | None = Field(
        default=None,
        foreign_key="author.id_",
        primary_key=True,
    )
    book_fk: int | None = Field(
        default=None,
        foreign_key="book.id_",
        primary_key=True,
    )

    author: Author = Relationship(back_populates="link_book")
    book: Book = Relationship(back_populates="link_author")


class AuthorBookCreate(AuthorBookBase):
    pass


class AuthorBookRead(SQLModel):
    name: str
    title: str


class AuthorBookUpdate(AuthorBookBase):
    pass


class AuthorBookDelete(AuthorBookBase):
    pass
