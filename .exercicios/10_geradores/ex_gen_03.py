"""Exercício 03.

Crie um gerador chamado gerador_telefones que produza uma sequência infinita de
números de telefone aleatórios.
Os números de telefone devem seguir o formato padrão do Brasil, contendo o código de
área, o prefixo e os dígitos finais.
Em seguida, utilize um loop for para imprimir as primeiras 5 sequências de números de
telefone geradas pelo seu gerador.
"""

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import NoReturn


def gerador_telefones(fixo: bool = True) -> "Generator[str, None, NoReturn]":
    while True:
        ddd: int = random.randint(a=11, b=99)

        digitos_finais: int = random.randint(a=0, b=9999)

        if fixo:
            prefixo: int = random.randint(a=2, b=5)
            segudo_digito_prefixo: int = random.randint(a=0, b=999)

            telefone: str = (
                f"({ddd}) {prefixo}{segudo_digito_prefixo:03d}-{digitos_finais:04d}"
            )
        else:
            prefixo = 9
            segudo_digito_prefixo = random.randint(a=0, b=9999)

            telefone = (
                f"({ddd}) {prefixo}{segudo_digito_prefixo:04d}-{digitos_finais:04d}"
            )

        yield telefone


gerador_fixo: "Generator[str, None, NoReturn]" = gerador_telefones(fixo=True)

gerador_celular: "Generator[str, None, NoReturn]" = gerador_telefones(fixo=False)


print("As primeiras 5 sequências de números de telefone fixos:")
for _ in range(5):
    print(next(gerador_fixo))

print("\nAs primeiras 5 sequências de números de telefone móveis:")
for _ in range(5):
    print(next(gerador_celular))
