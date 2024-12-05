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

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print(
    random.choices(
        population=string.ascii_letters + string.digits + string.punctuation,
        k=10,
    ),
)
