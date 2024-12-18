from crud_entidades import AUTORES_ENDPOINT, LIVROS_ENDPOINT, remover_entidade


def remover_autor(id_: int) -> None:
    resultado: str | dict[str, str] = remover_entidade(
        id_=id_,
        endpoint=AUTORES_ENDPOINT,
    )

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Erro ao remover autor: {resultado['detail']}")


def remover_livro(id_: int) -> None:
    resultado: str | dict[str, str] = remover_entidade(
        id_=id_,
        endpoint=LIVROS_ENDPOINT,
    )

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Erro ao remover livro: {resultado['detail']}")


remover_autor(id_=2)
remover_livro(id_=3)
