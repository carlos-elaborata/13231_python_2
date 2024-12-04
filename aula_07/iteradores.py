from collections.abc import Iterator
from typing import Self


class Cores:
    def __init__(self) -> None:
        self.cores: list[str] = [
            "vermelho",
            "verde",
            "violeta",
            "azul",
            "branco",
            "amarelo",
        ]
        self.indice: int = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> str:
        if self.indice < len(self.cores):
            cor_atual: str = self.cores[self.indice]
            self.indice += 1
            return cor_atual
        self.indice = 0
        raise StopIteration


cores = Cores()

# for cor in cores:
#     print(cor)


class MeuIteravel:
    def __init__(self, nome: str, dados: list[int]) -> None:
        self.nome: str = nome
        self.dados: list[int] = dados
        self.indice = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.indice < len(self.dados):
            valor: int = self.dados[self.indice]
            self.indice += 1
            return valor
        self.indice = 0
        print("Fim da iteração.")
        raise StopIteration


meu_iteravel = MeuIteravel(nome="Minha Lista", dados=[5, 4, 3, 2, 1])

# print("Usando um loop for:")
# for numero in meu_iteravel:
#     print(numero)

# print("\nUsando a função next():")
# while True:
#     try:
#         numero: int = next(meu_iteravel)
#         print(numero)
#     except StopIteration:
#         break


class IteradorDict:
    def __init__(self, dicionario: dict[str, int]) -> None:
        self.chaves: list[str] = list(dicionario.keys())
        self.valores: list[int] = list(dicionario.values())
        self.indice: int = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> tuple[str, int]:
        if self.indice < len(self.chaves):
            chave: str = self.chaves[self.indice]
            valor: int = self.valores[self.indice]
            self.indice += 1
            return chave, valor
        self.indice = 0
        raise StopIteration


meu_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}

iterador_dict = IteradorDict(dicionario=meu_dict)

# for chave, valor in iterador_dict:
#     print(chave, valor)

numeros: list[int] = [1, 2, 3, 4, 5]

# for numero in numeros:
#     print(numero)

iterador: Iterator[int] = iter(numeros)
while True:
    try:
        numero: int = next(iterador)
        print(numero)
    except StopIteration:
        break
