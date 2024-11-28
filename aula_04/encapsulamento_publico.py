class Carro:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo

    def descricao(self) -> str:
        return f"Este é um carro {self.marca} {self.modelo}."


carro = Carro(marca="Honda", modelo="Civic")
print(carro.marca)
print(carro.modelo)
print(carro.descricao())

carro.marca = "Toyota"
print(carro.descricao())

carro.modelo = "Hilux"
print(carro.descricao())
print(carro.__dict__)
