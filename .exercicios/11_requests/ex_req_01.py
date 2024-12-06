"""Exercício 01.

Crie uma requisição do tipo GET para o endpoint /get do serviço httpbin.org.
Envie dados de um objeto do tipo Cliente como parâmetros na solicitação.
Utilize dataclass para definir a estrutura do objeto Cliente.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from requests import Response


@dataclass
class Cliente:
    nome: str
    idade: int
    email: str


cliente = Cliente(nome="João", idade=30, email="joao@pudim.com.br")

url = "https://httpbin.org/get"

params: dict[str, str | int] = cliente.__dict__
print(cliente)

resposta: "Response" = requests.get(url=url, params=params, timeout=10)

print(resposta.text)
