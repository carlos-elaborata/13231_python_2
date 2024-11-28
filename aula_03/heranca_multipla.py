class Pai:
    def __init__(self) -> None:
        self.nome_pai: str = "João"

    def mensagem_pai(self) -> str:
        return f"Oi, eu sou o pai de nome {self.nome_pai}."


class Mae:
    def __init__(self) -> None:
        self.nome_mae: str = "Maria"

    def mensagem_mae(self) -> str:
        return f"Oi, eu sou a mãe de nome {self.nome_mae}."


class Filho(Pai, Mae):
    def __init__(self) -> None:
        Pai.__init__(self=self)
        Mae.__init__(self=self)
        self.nome_filho: str = "Pedro"

    def mensagem_filho(self) -> str:
        return f"Oi, eu sou o filho de nome {self.nome_filho}."


pai = Pai()
mae = Mae()
filho = Filho()

print(pai.nome_pai)
print(pai.mensagem_pai(), "\n")

print(mae.nome_mae)
print(mae.mensagem_mae(), "\n")

print(filho.mensagem_pai())
print(filho.mensagem_mae())
print(filho.mensagem_filho())
print(filho.nome_pai)
print(filho.nome_mae)
print(filho.nome_filho)
