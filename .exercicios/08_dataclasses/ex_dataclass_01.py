"""Exercício 01.

Crie uma aplicação para gerenciar um inventário de uma loja.
Cada produto no inventário deve ser representado por uma dataclass contendo as
seguintes informações: nome do produto, preço unitário e quantidade em estoque.
Em seguida, crie uma classe Inventario e implemente métodos para adicionar novos
produtos ao inventário, atualizar a quantidade em estoque e calcular o valor total do
inventário.
"""

from dataclasses import dataclass, field


@dataclass
class Produto:
    pass


@dataclass
class Inventario:
    produtos: list[Produto] = field(default_factory=list)

    def adicionar_produto(self, produto: Produto) -> None:
        pass

    def atualizar_estoque(self, nome_produto: str, quantidade: int) -> None:
        pass

    def calcular_valor_total(self) -> float:
        pass
