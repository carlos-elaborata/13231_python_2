from crud_entidades import (
    AUTORES_ENDPOINT,
    LIVROS_ENDPOINT,
    atualizar_entidade_parcial,
    atualizar_entidade_total,
)

autor_atualizado_parcial: dict[str, str | list[int]] = {"name": "Joanne Rowling"}
autor_atualizado_total: dict[str, str | list[int]] = {"name": "Joanne K. Rowling"}

livro_atualizado_parcial: dict[str, str | list[int]] = {"title": "Novo Livro Parcial"}
livro_atualizado_total: dict[str, str | list[int]] = {
    "title": "Novo Livro Total",
    "genre": "Novo Gênero Total",
    "isbn": "1234567890",
    "authors_ids": [1, 2, 3],
}


def atualizar_autor_parcial(
    id_: int,
    autor_atualizado: dict[str, str | list[int]],
) -> None:
    autor: dict[str, str | int | list[dict[str, str | int]]] = (
        atualizar_entidade_parcial(
            id_=id_,
            entidade=autor_atualizado,
            endpoint=AUTORES_ENDPOINT,
        )
    )

    print("\nAutor atualizado (parcial):")
    print(f"ID: {autor['id_']}")
    print(f"  Autor: {autor['name']}")


def atualizar_autor_total(
    id_: int,
    autor_atualizado: dict[str, str | list[int]],
) -> None:
    autor: dict[str, str | int | list[dict[str, str | int]]] = atualizar_entidade_total(
        id_=id_,
        entidade=autor_atualizado,
        endpoint=AUTORES_ENDPOINT,
    )

    print("Autor atualizado (total):")
    print(f"ID: {autor['id_']}")
    print(f"  Autor: {autor['name']}")


def atualizar_livro_parcial(
    id_: int,
    livro_atualizado: dict[str, str | list[int]],
) -> None:
    livro: dict[str, str | int | list[dict[str, str | int]]] = (
        atualizar_entidade_parcial(
            id_=id_,
            entidade=livro_atualizado,
            endpoint=LIVROS_ENDPOINT,
        )
    )

    print("\nLivro atualizado (parcial):")
    print(f"ID: {livro['id_']}")
    print(f"  Título: {livro['title']}")
    print(f"  Gênero: {livro['genre']}")
    print(f"  ISBN: {livro['isbn']}")


def atualizar_livro_total(
    id_: int,
    livro_atualizado: dict[str, str | list[int]],
) -> None:
    livro: dict[str, str | int | list[dict[str, str | int]]] = atualizar_entidade_total(
        id_=id_,
        entidade=livro_atualizado,
        endpoint=LIVROS_ENDPOINT,
    )

    print("\nLivro atualizado (total):")
    print(f"ID: {livro['id_']}")
    print(f"  Título: {livro['title']}")
    print(f"  Gênero: {livro['genre']}")
    print(f"  ISBN: {livro['isbn']}")


# atualizar_autor_parcial(id_=3, autor_atualizado=autor_atualizado_parcial)
# atualizar_autor_total(id_=3, autor_atualizado=autor_atualizado_total)
# atualizar_livro_parcial(id_=3, livro_atualizado=livro_atualizado_parcial)
atualizar_livro_total(id_=4, livro_atualizado=livro_atualizado_total)
