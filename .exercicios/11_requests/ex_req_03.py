"""Exercício 03.

Crie uma função chamada consultar_ultimos_artigos que realiza uma consulta à API v4
do Spaceflight News (spaceflightnewsapi.net) para obter os últimos artigos publicados.
A função deve imprimir os títulos dos 5 primeiros artigos retornados pela API.
Se ocorrer algum erro na consulta, a função deve imprimir uma mensagem informando a
falha na solicitação.
"""

from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from requests import Response

URL = "https://api.spaceflightnewsapi.net/v4/articles"


def consultar_ultimos_artigos(limite: int = 5) -> None:
    parametros: dict[str, int] = {"limit": limite}

    resposta: Response = requests.get(url=URL, params=parametros, timeout=10)

    if resposta.ok:
        dados: dict[
            str,
            int
            | str
            | list[dict[str, int | str | bool | list[dict[str, str | int]]]]
            | None,
        ] = resposta.json()

        if isinstance(dados["results"], list):
            resultados: list[
                dict[str, int | str | bool | list[dict[str, str | int]]]
            ] = dados["results"]

            for artigo in resultados:
                print(artigo["title"])

    else:
        print(f"Falha na solicitação: Erro código {resposta.status_code}.")


consultar_ultimos_artigos()
