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
    nome: str
    descricao: str
    status: str = "A Fazer"

    def __post_init__(self) -> None:
        if self.status not in {"A Fazer", "Em Andamento", "Concluída"}:
            msg = (
                "O status da tarefa deve ser 'A Fazer', 'Em Andamento' ou 'Concluída'."
            )
            raise ValueError(msg)


@dataclass
class Projeto:
    tarefas: list[Tarefa] = field(default_factory=list)

    def adicionar_tarefa(self, nova_tarefa: Tarefa) -> None:
        for t in self.tarefas:
            if t.nome == nova_tarefa.nome and t.status == nova_tarefa.status:
                msg: str = f"Tarefa '{t.nome}' com status '{t.status}' já existe."
                raise ValueError(msg)
        self.tarefas.append(nova_tarefa)

    def alterar_status(self, nome_tarefa: str, novo_status: str) -> None:
        for t in self.tarefas:
            if t.nome == nome_tarefa:
                if novo_status not in {"A Fazer", "Em Andamento", "Concluída"}:
                    msg = (
                        "O novo status da tarefa deve ser 'A Fazer', 'Em Andamento' ou"
                        " 'Concluída'."
                    )
                    raise ValueError(msg)
                t.status = novo_status
                return
        msg: str = f"Tarefa '{nome_tarefa}' não encontrada no projeto."
        raise ValueError(msg)

    def listar_tarefas(self) -> None:
        for t in self.tarefas:
            print(f"Nome: {t.nome}\n\tDescrição: {t.descricao}\n\tStatus: {t.status}")


projeto = Projeto()

projeto.adicionar_tarefa(
    nova_tarefa=Tarefa(
        nome="Implementar login",
        descricao="Implementar sistema de login no site",
    ),
)

projeto.adicionar_tarefa(
    nova_tarefa=Tarefa(
        nome="Corrigir bugs",
        descricao="Corrigir bugs encontrados na fase de testes",
        status="Em Andamento",
    ),
)

projeto.listar_tarefas()

projeto.alterar_status(nome_tarefa="Corrigir bugs", novo_status="Concluída")

projeto.listar_tarefas()
