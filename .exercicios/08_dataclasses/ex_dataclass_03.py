"""Exercício 03.

Crie um sistema para registrar informações dos alunos em uma escola.
Cada aluno deve ser representado por uma dataclass contendo nome, idade, série e notas
em diferentes disciplinas.
Implemente uma classe Escola e métodos para adicionar novos alunos, calcular a média de
notas de um aluno e listar todos os alunos registrados.
"""

from dataclasses import dataclass, field


@dataclass
class Aluno:
    nome: str
    idade: int
    serie: int
    notas: dict[str, float]


@dataclass
class Escola:
    alunos: list[Aluno] = field(default_factory=list)

    def adicionar_aluno(self, aluno: Aluno) -> None:
        pass

    def calcular_media_notas(self, nome_aluno: str) -> float:
        pass

    def listar_alunos(self) -> None:
        pass
