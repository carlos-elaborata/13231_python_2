from crud_entidades import (
    AUTORES_ENDPOINT,
    LIVROS_ENDPOINT,
    ler_por_id_entidade,
    ler_todas_entidades,
)


def ler_autor(id_: int) -> None:
    autor: dict[str, str | int | list[dict[str, str | int]]] = ler_por_id_entidade(
        id_=id_,
        endpoint=AUTORES_ENDPOINT,
    )

    print(f"ID: {autor['id_']}")
    print(f"  Autor: {autor['name']}")

    if isinstance(autor["books"], list):
        for livro in autor["books"]:
            print(f"    Título: {livro['title']}")
            print(f"      Gênero: {livro['genre']}")
            print(f"      ISBN: {livro['isbn']}")


def ler_livro(id_: int) -> None:
    livro: dict[str, str | int | list[dict[str, str | int]]] = ler_por_id_entidade(
        id_=id_,
        endpoint=LIVROS_ENDPOINT,
    )

    print(f"ID: {livro['id_']}")
    print(f"  Título: {livro['title']}")
    print(f"  Gênero: {livro['genre']}")
    print(f"  ISBN: {livro['isbn']}")

    if isinstance(livro["authors"], list):
        for autor in livro["authors"]:
            print(f"    Autor: {autor['name']}")


def ler_autores() -> None:
    lista_autores: list[dict[str, str | int | list[dict[str, str | int]]]] = (
        ler_todas_entidades(endpoint=AUTORES_ENDPOINT)
    )

    print("\nLista de autores:")

    for autor in lista_autores:
        print(f"ID: {autor['id_']}")
        print(f"  Autor: {autor['name']}")
        print("  Livros:")

        if isinstance(autor["books"], list):
            for livro in autor["books"]:
                print(f"    Título: {livro['title']}")


def ler_livros() -> None:
    lista_livros: list[dict[str, str | int | list[dict[str, str | int]]]] = (
        ler_todas_entidades(endpoint=LIVROS_ENDPOINT)
    )

    print("\nLista de livros:")

    for livro in lista_livros:
        print(f"ID: {livro['id_']}")
        print(f"  Título: {livro['title']}")
        print(f"  Gênero: {livro['genre']}")
        print(f"  ISBN: {livro['isbn']}")
        print("  Autores:")

        if isinstance(livro["authors"], list):
            for autor in livro["authors"]:
                print(f"    Autor: {autor['name']}")


ler_autor(id_=1)
ler_livro(id_=23)
ler_autores()
ler_livros()
