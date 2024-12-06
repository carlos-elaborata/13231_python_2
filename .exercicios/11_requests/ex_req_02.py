"""Exercício 02.

Crie uma função chamada consultar_cep que recebe um CEP como argumento e consulte
informações sobre esse CEP utilizando a API do ViaCEP (viacep.com.br).
A função deve imprimir os detalhes do endereço correspondente ao CEP fornecido.
Se o CEP não for encontrado, deve imprimir uma mensagem informando que o CEP não foi
encontrado.
"""

import requests


def consultar_cep(cep: str) -> None:
    url: str = f"https://viacep.com.br/ws/{cep}/json/"

    responsta = requests.get(url, timeout=10)

    print(responsta.status_code)

    data = responsta.json()

    print("CEP encontrado:")
    print(f"CEP: {data['cep']}")
    print(f"Logradouro: {data['logradouro']}")
    print(f"Complemento: {data['complemento']}")
    print(f"Bairro: {data['bairro']}")
    print(f"Cidade: {data['localidade']}")
    print(f"Estado: {data['estado']}")


cep: str = input("Digite o CEP para consulta: ")
consultar_cep(cep=cep)
