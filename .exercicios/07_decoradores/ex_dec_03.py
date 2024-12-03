"""Exercício 03.

Você está desenvolvendo um sistema de gerenciamento de pedidos para uma loja.
Você precisa implementar uma funcionalidade que permita calcular o valor total de um
pedido, com a opção de aplicar um desconto se necessário.
Para isso, você decidiu usar um decorador chamado aplicar_desconto, que pode ser
aplicado ao método calcular_total da classe Pedido.

O decorador aplicar_desconto recebe dois parâmetros opcionais: desconto e
valor_desconto.
Se desconto for True, o decorador aplicará o desconto ao valor total do pedido com base
no valor_desconto fornecido.
Caso contrário, o valor total do pedido será calculado sem desconto.

Sua tarefa é implementar o decorador aplicar_desconto e a classe Pedido de acordo com
as especificações fornecidas.
"""

# Importa TYPE_CHECKING para evitar importações circulares durante a verificação de
# tipos
from typing import TYPE_CHECKING

# Verifica se o código está sendo analisado por um verificador de tipos
if TYPE_CHECKING:
    # Importa Callable para anotações de tipo dentro do decorador
    from collections.abc import Callable


def aplicar_desconto(func: "Callable[..., float]") -> "Callable[..., float]":
    """Decorador que aplica um desconto ao valor total calculado pela função decorada.

    Args:
        func (Callable[..., float]): A função original que calcula o valor total do
        pedido.

    Returns:
        Callable[..., float]: A função decorada que inclui a lógica de desconto.
    """

    def wrapper(
        pedido: "Pedido",
        /,
        *,
        desconto: bool = False,
        valor_desconto: float = 0,
    ) -> float:
        """Envolve a função original para adicionar a funcionalidade de desconto.

        Args:
            pedido (Pedido): A instância da classe Pedido para a qual o total será
            calculado.
            desconto (bool, optional): Flag indicando se um desconto deve ser aplicado.
            O padrão é False.
            valor_desconto (float, optional): O valor do desconto a ser aplicado (como
            um decimal, por exemplo, 0.05 para 5%). O padrão é 0.

        Returns:
            float: O valor total do pedido, possivelmente com desconto aplicado.
        """
        # Chama a função original para calcular o valor total sem desconto
        total: float = func(pedido)

        # Verifica se o desconto deve ser aplicado
        if desconto:
            # Aplica o desconto multiplicando o total pelo fator de desconto
            total *= 1 - valor_desconto

        # Retorna o valor total, com ou sem desconto.
        return total

    # Retorna a função wrapper que envolve a função original
    return wrapper


class Pedido:
    """Classe que representa um pedido em uma loja.

    Utiliza um decorador para adicionar a funcionalidade de desconto ao cálculo do total
    do pedido.

    Attributes:
        itens (list[dict[str, float]]): Lista de itens no pedido, onde cada item é um
        dicionário contendo o preço.
    """

    def __init__(self, itens: list[dict[str, float]]) -> None:
        """Construtor da classe Pedido.

        Args:
            itens (list[dict[str, float]]): Lista de itens no pedido. Cada item deve ser
            um dicionário com a chave "preco" mapeando para um float.
        """
        # Atributo que armazena os itens do pedido
        self.itens: list[dict[str, float]] = itens

    # Aplica o decorador para adicionar a funcionalidade de desconto ao método
    # calcular_total
    @aplicar_desconto
    def calcular_total(self) -> float:
        """Calcula o valor total do pedido somando os preços de todos os itens.

        Returns:
            float: A soma dos preços de todos os itens no pedido.
        """
        # Calcula a soma dos preços de todos os itens no pedido
        return sum(item["preco"] for item in self.itens)


# Cria uma instância da classe Pedido com uma lista de itens, cada um com um preço
# específico
pedido_1 = Pedido(itens=[{"preco": 50}, {"preco": 30}, {"preco": 20}])

# Calcula e imprime o total do pedido sem aplicar desconto
print(f"Total s/ desconto: R$ {pedido_1.calcular_total():.2f}")
# Esperado: 100

# Calcula e imprime o total do pedido aplicando um desconto de 5%
print(
    "Total c/ desconto: R$ "
    f"{pedido_1.calcular_total(desconto=True, valor_desconto=0.05):.2f}",
)
# Esperado: 95
