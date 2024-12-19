from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class BaseModel(SQLModel):
    """Modelo base para definir a chave primária das entidades."""

    # Define o campo `id_` como chave primária.
    # - `default=None`: Permite que o ID seja gerado automaticamente pelo banco de
    #   dados.
    # - `primary_key=True`: Especifica que este campo é a chave primária da tabela.
    id_: int | None = Field(default=None, primary_key=True)


class AuthorBase(SQLModel):
    """Modelo base para definir os campos de um autor."""

    # Define o campo `name` como string, com indexação no banco de dados.
    # - `index=True`: Cria um índice para melhorar a performance de buscas por este
    #   campo.
    name: str = Field(index=True)


class BookBase(SQLModel):
    """Modelo base para definir os campos de um livro."""

    # Define o título do livro como uma string.
    # - `index=True`: Cria um índice para facilitar buscar
    title: str = Field(index=True)

    # Define o gênero do livro como uma string.
    genre: str

    # Define o ISBN do livro como uma string.
    isbn: str

    # Adiciona um validador para o campo `isbn`.
    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, value: str) -> str:
        """Valida o campo ISBN, garantindo que tenha 10 ou 13 caracteres.

        Args:
            value (str): Valor do ISBN fornecido.

        Raises:
            ValueError: Se o ISBN não tiver 10 ou 13 caracteres.

        Returns:
            str: O ISBN limpo (sem hífens), caso seja válido.
        """
        # Remove hífens do ISBN para padronização.
        clean_isbn: str = value.replace("-", "")

        # Verifica se o ISBN tem o comprimento correto.
        # - Um ISBN válido deve ter 10 ou 13 caracteres.
        if len(clean_isbn) not in {10, 13}:
            msg = "O ISBN deve conter 10 ou 13 caracteres."
            raise ValueError(msg)

        # Retorna o ISBN limpo.
        return clean_isbn


class AuthorBook(SQLModel, table=True):
    """Tabela associativa para representar a relação entre autores e livros."""

    # Define a chave estrangeira que referencia a tabela `author`.
    # - `foreign_key="author.id_"`: Especifica que este campo está relacionado ao campo
    #   `id_` da tabela `author`.
    # - `primary_key=True`: Gerante que a combinação `author_fk` + `book_fk` seja única.
    # - `ondelete="CASCADE"`: Configura a exclusão em cascata, para remover relações ao
    #   remover um autor.
    author_fk: int = Field(
        foreign_key="author.id_",
        primary_key=True,
        ondelete="CASCADE",
    )
    # Define a chave estrangeira que referencia a tabela `book`.
    # - `foreign_key="book.id_"`: Relaciona este campo ao campo `id_` da tabela `book`.
    # - `primary_key=True`: Faz parte da chave composta com `author_fk`.
    # - `ondelete="CASCADE"`: Remove relações ao remover um livro.
    book_fk: int = Field(
        foreign_key="book.id_",
        primary_key=True,
        ondelete="CASCADE",
    )


class Author(BaseModel, AuthorBase, table=True):
    """Modelo que representa a tabela de autores no banco de dados."""

    # Define a relação entre autores e livros.
    # - `back_populates="authors"`: Garente que a relação seja bidirecional, permitindo
    # acesso mútuo.
    # - `link_model=AuthorBook`: Usa a tabela associativa `AuthorBook` para gerenciar a
    # relação.
    books: list["Book"] = Relationship(
        back_populates="authors",
        link_model=AuthorBook,
    )


class Book(BaseModel, BookBase, table=True):
    """Modelo que representa a tabela de livros no banco de dados."""

    # Define a relação entre livros e autores.
    # - `back_populates="books"`: Garente a relação bidirecional com autores.
    # - `link_model=AuthorBook`: Usa a tabela associativa `AuthorBook`.
    authors: list[Author] = Relationship(
        back_populates="books",
        link_model=AuthorBook,
    )


# Modelos para operações CRUD


class AuthorCreate(AuthorBase):
    """Modelo para criação de autores."""


class AuthorRead(BaseModel, AuthorBase):
    """Modelo para leitura de autores."""


class AuthorReadWithBooks(AuthorRead):
    """Modelo para leitura detalhada de autores com seus livros."""

    # Lista de livros associados a um autor.
    # - `default_factory=list`: Garante que, por padrão, será uma lista vazia.
    books: list["BookRead"] = Field(default_factory=list)


class AuthorPut(AuthorBase):
    """Modelo para atualização completa de autores."""


class AuthorPatch(SQLModel):
    """Modelo para atualização parcial de autores."""

    # Permite que o nome do autor seja alterado ou deixado como `None`.
    name: str | None = None


class BookCreate(BookBase):
    """Modelo para criação de livros."""

    # Lista de IDs de autores associados ao livro.
    # - Um livro pode ter vários autores, representados pelos seus IDs.
    authors_ids: list[int]


class BookRead(BaseModel, BookBase):
    """Modelo para leitura de livros."""


class BookReadWithAuthors(BookRead):
    """Modelo para leitura detalhada de livros com seus autores."""

    # Lista de autores associados a um livro.
    # - `default_factory=list`: Garante que, por padrão, será uma lista vazia.
    authors: list[AuthorRead] = Field(default_factory=list)


class BookPut(BookBase):
    """Modelo para atualização completa de livros."""

    # Lista de IDs de autores associados ao livro.
    # - Este campo substitui todos os autores atuais do livro.
    authors_ids: list[int]


class BookPatch(SQLModel):
    """Modelo para atualização parcial de livros."""

    # Campos opcionais para atualização parcial.
    # - `None` indica que o campo deve ser deixado inalterado.
    title: str | None = None
    genre: str | None = None
    isbn: str | None = None
    authors_ids: list[int] | None = None
