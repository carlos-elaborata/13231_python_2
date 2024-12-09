from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str
    _idade: int

    def __post_init__(self) -> None:
        if self._idade < 0:
            msg = "A idade não pode ser negativa."
            raise ValueError(msg)

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, nova_idade: int) -> None:
        if not isinstance(nova_idade, int):
            msg = "A idade deve ser um número inteiro."
            raise TypeError(msg)
        if nova_idade < 0:
            msg = "A idade não pode ser negativa."
            raise ValueError(msg)
        self._idade = nova_idade

    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos."


george_orwell = Pessoa("George Orwell", 46)
print(george_orwell)


try:
    george_orwell.idade = 30
    print(f"Nova idade de {george_orwell.nome}: {george_orwell.idade} anos.")
    george_orwell.idade = -5
except ValueError as e:
    print(f"Erro: {e}")

try:
    george_orwell.idade = "trinta"  # type: ignore[reportAttributeAccessIssue]
except TypeError as e:
    print(f"Erro: {e}")


@dataclass
class Biblioteca:
    nome: str
    livros: list["Livro"] = field(default_factory=list)

    def adicionar_livro(self, livro: "Livro") -> None:
        self.livros.append(livro)


@dataclass
class Livro:
    titulo: str
    autor: Pessoa
    preco: float


biblioteca = Biblioteca("Central")
print(biblioteca)

livro_1 = Livro("1984", george_orwell, 29.99)
livro_2 = Livro("A Revolução dos Bichos", george_orwell, 19.99)

biblioteca.adicionar_livro(livro_1)
biblioteca.adicionar_livro(livro_2)

print(biblioteca)
