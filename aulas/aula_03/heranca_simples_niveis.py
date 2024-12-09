class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo

    def descricao(self) -> str:
        return f"Veículo: {self.marca} {self.modelo}."


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str) -> None:
        super().__init__(marca=marca, modelo=modelo)
        self.cor: str = cor

    def descricao(self) -> str:
        return f"Carro: {self.marca} {self.modelo} Cor: {self.cor}."


class CarroEsportivo(Carro):
    def __init__(
        self,
        marca: str,
        modelo: str,
        cor: str,
        velocidade_maxima: float,
    ) -> None:
        super().__init__(marca=marca, modelo=modelo, cor=cor)
        self.velocidade_maxima: float = velocidade_maxima

    def descricao(self) -> str:
        return (
            f"Carro: {self.marca} {self.modelo} Cor: {self.cor}, Velocidade máxima: "
            f"{self.velocidade_maxima} km/h"
        )


carro = Carro(marca="Toyota", modelo="Hilux", cor="Preto")
print(carro.descricao())


carro_esportivo = CarroEsportivo(
    marca="Ferrari",
    modelo="488 GTB",
    cor="Vermelho",
    velocidade_maxima=330,
)
print(carro_esportivo.descricao())
