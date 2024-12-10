"""Exercício 02.

Você esteja desenvolvendo um aplicativo de análise de dados e precise testar uma
função que calcula a média de uma lista de valores.
Escreva testes usando pytest para garantir que a função calcula a média corretamente
para diferentes conjuntos de dados.
"""


def calcular_media(valores: list[float]) -> float:
    if not isinstance(valores, list):
        msg: str = "A entrada deve ser uma lista."
        raise TypeError(msg)

    try:
        return sum(valores) / len(valores)
    except TypeError as e:
        msg = "Todos os valores devem ser números."
        raise TypeError(msg) from e
    except ZeroDivisionError:
        return 0
