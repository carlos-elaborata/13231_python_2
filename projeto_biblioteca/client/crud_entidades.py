from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from requests import Response

API_BASE_URL = "http://127.0.0.1:8000/"
AUTORES_ENDPOINT = "autores/"
LIVROS_ENDPOINT = "livros/"


def criar_entidades(
    entidade: dict[str, str | list[int]],
    endpoint: str,
) -> dict[str, str | int | list[dict[str, str | int]]]:
    resposta: Response = requests.post(
        url=f"{API_BASE_URL}{endpoint}",
        json=entidade,
        timeout=10,
    )

    return resposta.json()


def ler_por_id_entidade(
    id_: int,
    endpoint: str,
) -> dict[str, str | int | list[dict[str, str | int]]]:
    resposta: Response = requests.get(
        url=f"{API_BASE_URL}{endpoint}{id_}",
        timeout=10,
    )

    return resposta.json()


def ler_todas_entidades(
    endpoint: str,
) -> list[dict[str, str | int | list[dict[str, str | int]]]]:
    resposta: Response = requests.get(
        url=f"{API_BASE_URL}{endpoint}",
        timeout=10,
    )

    return resposta.json()


def atualizar_entidade_parcial(
    id_: int,
    entidade: dict[str, str | list[int]],
    endpoint: str,
) -> dict[str, str | int | list[dict[str, str | int]]]:
    resposta: Response = requests.patch(
        url=f"{API_BASE_URL}{endpoint}{id_}",
        json=entidade,
        timeout=10,
    )

    return resposta.json()


def atualizar_entidade_total(
    id_: int,
    entidade: dict[str, str | list[int]],
    endpoint: str,
) -> dict[str, str | int | list[dict[str, str | int]]]:
    resposta: Response = requests.put(
        url=f"{API_BASE_URL}{endpoint}{id_}",
        json=entidade,
        timeout=10,
    )

    return resposta.json()


def remover_entidade(id_: int, endpoint: str) -> str | dict[str, str]:
    resposta: Response = requests.delete(
        url=f"{API_BASE_URL}{endpoint}{id_}",
        timeout=10,
    )

    if resposta.status_code == 204:
        if endpoint == AUTORES_ENDPOINT:
            return "Autor removido com sucesso."
        return "Livro removido com sucesso."

    return resposta.json()
