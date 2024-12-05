"""Exercício 02.

Crie um gerador chamado gerador_senhas que produza uma sequência infinita de senhas
aleatórias.
Cada senha deve conter uma combinação de letras maiúsculas, letras minúsculas, dígitos
e caracteres especiais.
Em seguida, utilize um loop for para imprimir as primeiras 5 senhas geradas pelo seu
gerador.
"""

import random
import string
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import NoReturn

caracteres_especiais = "!#$&*"


def gerador_senhas(tamanho: int = 8) -> "Generator[str, None, NoReturn]":
    while True:
        senha: str = "".join(
            random.choices(
                population=string.ascii_letters + string.digits + caracteres_especiais,
                k=tamanho,
            ),
        )

        yield senha


meu_gerador: "Generator[str, None, NoReturn]" = gerador_senhas(tamanho=10)

print("As primeiras 5 senhas geradas:")
for _ in range(5):
    print(next(meu_gerador))


meu_gerador_tamanho_8: "Generator[str, None, NoReturn]" = gerador_senhas()

print("As primeiras 5 senhas geradas com 8 caracteres:")
for _ in range(5):
    print(next(meu_gerador_tamanho_8))
