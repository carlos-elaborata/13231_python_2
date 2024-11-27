from decimal import Decimal


class Produto:
    def __init__(self, nome: str, preco: float, estoque: int) -> None:
        self.nome: str = nome
        self.preco: Decimal = Decimal(value=str(preco))
        self.estoque: int = estoque

    def aumentar_estoque(self, quantidade: int) -> None:
        if quantidade > 0:
            self.estoque += quantidade

    def diminuir_estoque(self, quantidade: int) -> None:
        if quantidade > 0:
            if quantidade > self.estoque:
                print("Quantidade indisponível em estoque.")
            else:
                self.estoque -= quantidade

    def calcular_valor_total(self) -> Decimal:
        return self.preco * self.estoque

    def descricao(self) -> str:
        return (
            f"Nome: {self.nome}\n  Preco: R$ {self.preco:.2f}\n  Quantidade em Estoque:"
            f" {self.estoque}\n  Valor Total do Estoque: R$ "
            f"{self.calcular_valor_total():.2f}"
        )
