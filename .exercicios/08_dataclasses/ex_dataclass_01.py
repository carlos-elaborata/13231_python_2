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
    nome: str
    preco: float
    quantidade: int


@dataclass
class Inventario:
    produtos: list[Produto] = field(default_factory=list)

    def adicionar_produto(self, produto: Produto) -> None:
        for p in self.produtos:
            if p.nome == produto.nome:
                print(f"Produto '{produto.nome}' já existe no inventário.")
                return
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao inventário.")

    def atualizar_estoque(self, nome_produto: str, quantidade: int) -> None:
        for p in self.produtos:
            if p.nome == nome_produto:
                p.quantidade += quantidade
                print(
                    f"Estoque do produto '{nome_produto}' atualizado para "
                    f"{p.quantidade}.",
                )
                return
        print(f"Produto '{nome_produto}' não encontrado no inventário.")

    def calcular_valor_total(self) -> float:
        valor_total: float = sum(
            produto.preco * produto.quantidade for produto in self.produtos
        )
        print(f"Valor total do inventário: R$ {valor_total:,.2f}")
        return valor_total


inventario = Inventario()

inventario.adicionar_produto(produto=Produto(nome="Camiseta", preco=20, quantidade=50))
inventario.adicionar_produto(produto=Produto(nome="Camiseta", preco=18, quantidade=55))
inventario.adicionar_produto(
    produto=Produto(nome="Calça Jeans", preco=50, quantidade=30),
)

inventario.atualizar_estoque(nome_produto="Camiseta", quantidade=20)
inventario.atualizar_estoque(nome_produto="Boné", quantidade=10)

inventario.calcular_valor_total()
