from dataclasses import dataclass


@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int

    def adicionar_estoque(self, quantidade: int) -> None:
        if quantidade > 0:
            self.estoque += quantidade

    def remover_estoque(self, quantidade: int) -> None:
        if quantidade > self.estoque:
            msg: str = "Quantidade solicitada maior que o estoque disponível."
            raise ValueError(msg)

        self.estoque -= quantidade
