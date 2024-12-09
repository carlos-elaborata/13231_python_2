from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.ano: int = ano

    @abstractmethod
    def acelerar(self) -> None:
        pass

    @abstractmethod
    def frear(self) -> None: ...


class Carro(Veiculo):
    def acelerar(self) -> None:
        print(f"O carro {self.marca} {self.modelo} está acelerando.")

    def frear(self) -> None:
        print(f"O carro {self.marca} {self.modelo} está freando.")


class Moto(Veiculo):
    def acelerar(self) -> None:
        print(f"A moto {self.marca} {self.modelo} está acelerando.")

    def frear(self) -> None:
        print(f"A moto {self.marca} {self.modelo} está freando.")


carro = Carro(marca="Toyota", modelo="Corolla", ano=2020)
# carro.acelerar()
# carro.frear()

moto = Moto(marca="Honda", modelo="CB500", ano=2019)
# moto.acelerar()
# moto.frear()


veiculos: list[Carro | Moto] = [carro, moto]

for veiculo in veiculos:
    veiculo.acelerar()
    veiculo.frear()
