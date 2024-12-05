"""Exercício 01.

Crie um gerador chamado gerador_pares que produza uma sequência infinita de números
pares, começando pelo número 2 e gerando os próximos números pares a partir dele.
Em seguida, utilize um loop for para imprimir os primeiros 10 números pares gerados
pelo seu gerador.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import NoReturn


def gerador_pares() -> "Generator[int, None, NoReturn]":
    numero: int = 2
    while True:
        yield numero
        numero += 2


meu_gerador: "Generator[int, None, NoReturn]" = gerador_pares()

print("Os primeiros 10 números pares:")
for i in range(10):
    print(f"{i + 1}º número par: {next(meu_gerador)}")

print("Os próximos 10 números pares:")
for i in range(10):
    print(f"{i + 1}º número par: {next(meu_gerador)}")
