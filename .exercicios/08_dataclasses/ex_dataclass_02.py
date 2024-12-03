"""Exercício 02.

Desenvolva uma aplicação para gerenciar tarefas em um projeto.
Cada tarefa deve ser representada por uma dataclass contendo o nome da tarefa, sua
descrição e o status atual (por exemplo, "A Fazer", "Em Andamento" ou "Concluída").
Implemente uma classe Projeto e métodos para adicionar novas tarefas, alterar o status
das tarefas e listar todas as tarefas do projeto.
"""

from dataclasses import dataclass, field


@dataclass
class Tarefa:
    pass

    def __post_init__(self) -> None:
        pass


@dataclass
class Projeto:
    tarefas: list[Tarefa] = field(default_factory=list)

    def adicionar_tarefa(self, nova_tarefa: Tarefa) -> None:
        pass

    def alterar_tarefa(self, nome_tarefa: str, novo_status: str) -> None:
        pass

    def listar_tarefas(self) -> None:
        pass
