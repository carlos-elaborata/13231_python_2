class Aluno:
    """Representa um aluno com os atributos nome, idade e disciplinas matriculadas.

    Permite a gestâo das disciplinas através de métodos para adicionar, remover e
    verificar a matrícula em disciplinas específicas.

    Attributes:
        nome (str): O nome do aluno.
        idade (int): A idade do aluno.
        disciplinas (list[str]): Uma lista de disciplinas matriculadas pelo aluno.
    """

    def __init__(self, nome: str, idade: int) -> None:
        """Inicializa um novo aluno com nome, idade e uma lista vazia de disciplinas.

        Args:
            nome (str): O nome do aluno.
            idade (int): A idade do aluno.
        """
        self.nome: str = nome
        self.idade: int = idade
        self.disciplinas: list[str] = []

    def adicionar_disciplina(self, disciplina: str) -> str:
        """Adiciona uma disciplina à lista do aluno, se ainda não matriculado.

        Args:
            disciplina (str): O nome da disciplina a ser matriculada.

        Raises:
            ValueError: Se o aluno já está matriculado na disciplina.

        Returns:
            str: Mensagem de matricula bem sucedida.
        """
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            return f"Disciplina {disciplina} adicionada para o aluno {self.nome}."
        msg_erro: str = (
            f"O aluno {self.nome} já está matriculado na disciplina {disciplina}."
        )
        raise ValueError(msg_erro)

    def remover_disciplina(self, disciplina: str) -> str:
        """Remove uma disciplina à lista do aluno, se estiver matriculado.

        Args:
            disciplina (str): O nome da disciplina a ser removida.

        Raises:
            ValueError: Se o aluno não está matriculado na disciplina.

        Returns:
            str: Mensagem de matricula removida com sucesso.
        """
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            return f"Disciplina {disciplina} removida para o aluno {self.nome}."
        msg_erro: str = (
            f"O aluno {self.nome} não está matriculado na disciplina {disciplina}."
        )
        raise ValueError(msg_erro)

    def verificar_disciplina(self, disciplina: str) -> str:
        """Verifica se o aluno está matriculado em uma disciplina específica.

        Args:
            disciplina (str): O nome da disciplina a ser verificada.

        Returns:
            str: Se o aluno está matriculado na disciplina ou não.
        """
        if disciplina in self.disciplinas:
            return f"O aluno {self.nome} está matriculado na disciplina {disciplina}."
        return f"O aluno {self.nome} não está matriculado na disciplina {disciplina}."
