"""Exercício 02.

Você está desenvolvendo um sistema de análise de vendas para uma empresa.
Crie um iterador IteradorVendasMensais que percorra uma lista de vendas mensais.
Cada venda é representada como um dicionário contendo informações como mês, valor total
e categoria do produto vendido.
A implementação do método next() deve permitir percorrer as vendas registradas e
retornar a próxima venda na lista.
No entanto, o iterador deve filtrar as vendas apenas para uma categoria específica de
produtos e, se encontrar uma venda com valor total superior a um limite específico,
deve retornar essa venda.
Caso contrário, ele deve pular para a próxima venda até encontrar uma que atenda aos
critérios definidos.
"""

# Importação do módulo typing para suporte a anotações de tipo
from typing import TYPE_CHECKING, Self

# Verifica se o código está sendo analisado por um verificador de tipos
if TYPE_CHECKING:
    # Importação de Iterator para tipagem de iteradores
    from collections.abc import Iterator


class IteradorVendasMensais:
    """Iterador para filtrar vendas mensais por categoria e valor mínimo.

    Este iterador percorre uma lista de vendas mensais e retorna apenas as vendas que
    pertencem a uma categoria específica e que possuem um valor total superior ou igual
    a um valor mínimo definido.

    Attributes:
        vendas (dict[str, dict[str, int]]): Dicionário com vendas mensais por categoria.
        categoria_alvo (str): Categoria de produto a ser filtrada.
        valor_minimo (int): Valor mínimo de venda para filtrar.
        meses_iter (Iterator[str]): Iterador sobre os meses das vendas.
    """

    def __init__(
        self,
        vendas: dict[str, dict[str, int]],
        categoria_alvo: str,
        valor_minimo: int,
    ) -> None:
        """Inicializa o iterador com vendas, categoria alvo e valor mínimo.

        Args:
            vendas (dict[str, dict[str, int]]): Dicionário com vendas mensais.
            categoria_alvo (str): Categoria de produto a ser filtrada.
            valor_minimo (int): Valor mínimo de venda para filtrar.
        """
        self.vendas: dict[str, dict[str, int]] = vendas
        self.categoria_alvo: str = categoria_alvo
        self.valor_minimo: int = valor_minimo
        # Criação de um iterador sobre as chaves (meses) das vendas
        self.meses_iter: Iterator[str] = iter(self.vendas)

    def __iter__(self) -> Self:
        """Retorna o próprio iterador.

        Returns:
            Self: A própria instância do iterador.
        """
        return self

    def __next__(self) -> dict[str, str | int]:
        """Retorna a próxima venda que atende aos critérios.

        Raises:
            StopIteration: Se não houver mais vendas que atendam aos critérios.

        Returns:
            dict[str, str | int]: Dicionário com as informações da venda.
        """
        # Loop para encontrar a próxima venda que atenda aos critérios
        for mes in self.meses_iter:
            # Obtém as vendas do mês atual
            venda_mes: dict[str, int] = self.vendas[mes]

            # Verifica se a categoria alvo está presente no mês atual
            if self.categoria_alvo in venda_mes:
                # Obtém o valor da venda para a categoria alvo
                valor_venda: int = venda_mes[self.categoria_alvo]

                # Verifica se o valor da venda atende ao valor mínimo
                if valor_venda >= self.valor_minimo:
                    # Retorna um dicionário com os detalhes da venda
                    return {
                        "mes": mes,
                        "valor_total": valor_venda,
                        "categoria": self.categoria_alvo,
                    }
        # Lança uma exceção quando não hà mais itens para iterar
        raise StopIteration


# Dicionário com as vendas mensais por categoria
vendas_mensais: dict[str, dict[str, int]] = {
    "Janeiro": {"Eletrônicos": 1500, "Roupas": 2500, "Livros": 1800},
    "Fevereiro": {"Eletrônicos": 2000, "Roupas": 2200, "Livros": 2800},
    "Março": {"Eletrônicos": 1800, "Roupas": 2800, "Livros": 2200},
    "Abril": {"Eletrônicos": 2800, "Roupas": 2000, "Livros": 2500},
    "Maio": {"Eletrônicos": 2200, "Roupas": 3000, "Livros": 2300},
    "Junho": {"Eletrônicos": 2500, "Roupas": 2400, "Livros": 2600},
}

# Criação da instância do iterador com critérios definidos
iterador_vendas_mensais = IteradorVendasMensais(
    vendas=vendas_mensais,
    categoria_alvo="Eletrônicos",
    valor_minimo=2000,
)

# Iteração sobre as vendas que atendem aos critérios e impressão dos resultados
for v in iterador_vendas_mensais:
    print(v)
