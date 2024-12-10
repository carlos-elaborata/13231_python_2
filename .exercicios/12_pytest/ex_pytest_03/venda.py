from dataclasses import dataclass, field

from produto import Produto


@dataclass
class Venda:
    produto: Produto
    quantidade: int
    valor_total: float = field(init=False)

    def __post_init__(self) -> None:
        if self.produto is None:
            msg = "Produto não pode ser None."
            raise TypeError(msg)
        if self.quantidade is None:
            msg = "Quantidade não pode ser None."
            raise TypeError(msg)
        if self.quantidade <= 0:
            msg = "A quantidade de venda deve ser positiva."
            raise ValueError(msg)
        if self.quantidade > self.produto.estoque:
            msg = "Estoque insuficiente para a venda."
            raise ValueError(msg)

        self.valor_total = self.produto.preco * self.quantidade
        self.produto.remover_estoque(quantidade=self.quantidade)
