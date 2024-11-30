"""Exercício 01.

Desenvolva um decorador que verifique se o usuário está autenticado antes de
executar uma função específica.
Este decorador deve ser aplicado a funções que exigem autenticação prévia para
acesso.
"""

usuario_autenticado = False


def autenticacao_requerida(func):
    def wrapper(*args, **kwargs):
        pass

    return wrapper


@autenticacao_requerida
def funcao_protegida() -> None:
    print("Função protegida executada com sucesso.")


# Usuário não está autenticado -> Que a função original não seja executada
# <mensagem de erro>
funcao_protegida()


usuario_autenticado = True
# Usuário está autenticado -> Que a função original seja executada
# "Função protegida executada com sucesso."
funcao_protegida()
