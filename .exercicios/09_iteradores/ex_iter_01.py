"""Exercício 01.

Você está desenvolvendo um sistema de gerenciamento de estoque para uma loja.
Crie um iterador chamado IteradorEstoque que percorra uma lista de produtos em estoque.
Cada produto é representado como um dicionário contendo informações como nome, preço e
quantidade disponível.
A implementação do método next() deve permitir percorrer os produtos disponíveis e
retornar o próximo produto na lista cujo estoque seja maior do que zero.
"""

from typing import Self


class IteradorEstoque:
    def __init__(self, produtos: list[dict[str, str | float]]) -> None:
        self.produtos: list[dict[str, str | float]] = produtos
        self.indice: int = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> dict[str, str | float]:
        while self.indice < len(self.produtos):
            produto: dict[str, str | float] = self.produtos[self.indice]

            self.indice += 1

            if isinstance(produto["quantidade"], int) and produto["quantidade"] > 0:
                return produto

        self.indice = 0

        raise StopIteration


estoque: list[dict[str, str | float]] = [
    {"nome": "Camiseta", "quantidade": 10, "preco": 29.99},
    {"nome": "Calça", "quantidade": 0, "preco": 59.99},
    {"nome": "Meia", "quantidade": 5, "preco": 39.99},
    {"nome": "Boné", "quantidade": 3, "preco": 19.99},
]

iterador_estoque = IteradorEstoque(produtos=estoque)

for produto in iterador_estoque:
    print(produto)
