from typing import Protocol


class Veiculo(Protocol):
    marca: str
    modelo: str
    ano: int

    def acelerar(self) -> None:
        pass

    def frear(self) -> None: ...


class Carro:
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.ano: int = ano

    def acelerar(self) -> None:
        print(f"O carro {self.marca} {self.modelo} está acelerando.")


class Moto:
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.ano: int = ano

    def acelerar(self) -> None:
        print(f"A moto {self.marca} {self.modelo} está acelerando.")

    def frear(self) -> None:
        print(f"A moto {self.marca} {self.modelo} está freando.")


carro = Carro(marca="Toyota", modelo="Corolla", ano=2020)
carro.acelerar()

moto = Moto(marca="Honda", modelo="CB500", ano=2019)
moto.acelerar()
moto.frear()
