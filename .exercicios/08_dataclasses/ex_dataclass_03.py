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
        self.alunos.append(aluno)
        print(f"Aluno '{aluno.nome}' adicionado à escola.")

    def calcular_media_notas(self, nome_aluno: str) -> float:
        for a in self.alunos:
            if a.nome == nome_aluno:
                soma_notas: float = sum(a.notas.values())
                qnt_notas: int = len(a.notas)
                media: float = soma_notas / qnt_notas
                media_arredondada: float = round(number=media, ndigits=2)
                return media_arredondada
        msg: str = f"Aluno '{nome_aluno}' não encontrado na escola."
        raise ValueError(msg)

    def listar_alunos(self) -> None:
        if not self.alunos:
            print("Nenhum aluno registrado na escola.")
            return
        for aluno in self.alunos:
            print(
                f"Nome: {aluno.nome}\n  Idade: {aluno.idade}\n  Série: {aluno.serie}"
                f"\n  Notas: ",
            )
            for d, n in aluno.notas.items():
                print(f"\tDisciplina: {d}\n\t  Nota: {n}")
            print(
                "  Média: "
                f"{Escola.calcular_media_notas(self=self, nome_aluno=aluno.nome)}",
            )


escola = Escola()

aluno_1 = Aluno(
    nome="João",
    idade=15,
    serie=9,
    notas={"Matemática": 8.5, "Ciências": 7.0, "História": 9.2},
)

aluno_2 = Aluno(
    nome="Maria",
    idade=14,
    serie=8,
    notas={"Matemática": 7.8, "Ciências": 6.50, "História": 8.0},
)


escola.adicionar_aluno(aluno=aluno_1)
escola.adicionar_aluno(aluno=aluno_2)

nome_aluno = "João"
print(
    f"Média das notas de {nome_aluno}: "
    f"{escola.calcular_media_notas(nome_aluno=nome_aluno)}",
)

escola.listar_alunos()
