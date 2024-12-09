"""Exercício 01.

Você está desenvolvendo uma aplicação de gerenciamento de tarefas e precisa testar a
função que adiciona uma nova tarefa à lista de tarefas.
Escreva testes usando pytest para garantir que a função se comporta corretamente ao
adicionar uma tarefa à lista.
"""

lista_tarefas: list[str] = []


def adicionar_tarefa(nova_tarefa: str) -> None:
    if not isinstance(nova_tarefa, str):
        msg: str = "A tarefa deve ser uma string."
        raise TypeError(msg)

    lista_tarefas.append(nova_tarefa)
