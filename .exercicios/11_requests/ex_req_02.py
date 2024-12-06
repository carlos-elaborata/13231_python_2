"""Exercício 02.

Crie uma função chamada consultar_cep que recebe um CEP como argumento e consulte
informações sobre esse CEP utilizando a API do ViaCEP (viacep.com.br).
A função deve imprimir os detalhes do endereço correspondente ao CEP fornecido.
Se o CEP não for encontrado, deve imprimir uma mensagem informando que o CEP não foi
encontrado.
"""

from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from requests import Response


def consultar_cep(cep: str) -> None:
    url: str = f"https://viacep.com.br/ws/{cep}/json/"

    responsta: Response = requests.get(url=url, timeout=0.1)
    responsta.raise_for_status()

    data: dict[str, str] = responsta.json()

    if "erro" in data:
        print("CEP não encontrado.")
    else:
        print("CEP encontrado:")
        print(f"CEP: {data['cep']}")
        print(f"Logradouro: {data['logradouro']}")
        print(f"Complemento: {data['complemento']}")
        print(f"Bairro: {data['bairro']}")
        print(f"Cidade: {data['localidade']}")
        print(f"Estado: {data['estado']}")


cep: str = input("Digite o CEP para consulta: ")
try:
    consultar_cep(cep=cep)
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except requests.exceptions.ConnectTimeout:
    print("Erro: Tempo esgotado.")
except requests.exceptions.RequestException as e:
    print(f"Erro: {e}")
