class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo

    def descricao(self) -> str:
        return f"Este é um veículo da marca {self.marca} e modelo {self.modelo}."


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str) -> None:
        super().__init__(marca=marca, modelo=modelo)
        self.cor: str = cor

    def descricao(self) -> str:
        return (
            f"Este é um carro da marca {self.marca}, modelo {self.modelo} e cor "
            f"{self.cor}."
        )


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cilindrada: int) -> None:
        super().__init__(marca=marca, modelo=modelo)
        self.cilindrada: int = cilindrada


veiculo = Veiculo(marca="X", modelo="Y2")
print(veiculo.descricao())

carro = Carro(marca="Toyota", modelo="Hilux", cor="Preto")
print(carro.descricao())
