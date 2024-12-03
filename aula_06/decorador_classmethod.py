from datetime import UTC, datetime
from typing import Self


class Pessoa:
    contador: int = 0

    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade
        Pessoa.contador += 1
        print(f"Pessoa criada: {self.nome}, Idade: {self.idade}")

    def __del__(self) -> None:
        Pessoa.contador -= 1
        print(f"Pessoa removida: {self.nome}, Idade: {self.idade}")
        del self

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}."

    @classmethod
    def obter_numero_de_pessoas(cls) -> int:
        return cls.contador

    @classmethod
    def criar_a_partir_ano_nascimento(cls, nome: str, ano_nascimento: int) -> Self:
        ano_atual: int = datetime.now(tz=UTC).year
        idade: int = ano_atual - ano_nascimento
        return cls(nome, idade)

    @classmethod
    def criar_anonimo(cls) -> Self:
        return cls("Anônimo", 0)


class Estudante(Pessoa):
    contador = 0

    def __init__(self, nome: str, idade: int, curso: str) -> None:
        super().__init__(nome=nome, idade=idade)
        self.curso: str = curso
        Estudante.contador += 1
        print("Esta pessoa é também um estudante.")

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso {self.curso}."

    @classmethod
    def obter_numero_de_estudantes(cls) -> int:
        return cls.contador

    @classmethod
    def criar_a_partir_ano_nascimento(  # type: ignore[reportIncompatibleMethodOverride]
        cls,
        nome: str,
        ano_nascimento: int,
        curso: str,
    ) -> Self:
        ano_atual: int = datetime.now(tz=UTC).year
        idade: int = ano_atual - ano_nascimento
        return cls(nome, idade, curso)


print(f"Número de pessoas: {Pessoa.obter_numero_de_pessoas()}")
print(f"Número de estudantes: {Estudante.obter_numero_de_pessoas()}")

pessoa_1 = Pessoa(nome="Alice", idade=30)
pessoa_2: Pessoa = Pessoa.criar_a_partir_ano_nascimento(
    nome="João",
    ano_nascimento=1990,
)
pessoa_3: Pessoa = Pessoa.criar_anonimo()

print(f"Número de pessoas: {Pessoa.obter_numero_de_pessoas()}")
print(f"Número de estudantes: {Estudante.obter_numero_de_pessoas()}")

del pessoa_3
print(f"Número de pessoas: {Pessoa.obter_numero_de_pessoas()}")

estudante_1 = Estudante(nome="Maria", idade=22, curso="Matemática")
estudante_2: Estudante = Estudante.criar_a_partir_ano_nascimento(
    nome="Vitória",
    ano_nascimento=1992,
    curso="História",
)

print(f"Número de pessoas: {Pessoa.obter_numero_de_pessoas()}")
print(f"Número de estudantes: {Estudante.obter_numero_de_pessoas()}")
