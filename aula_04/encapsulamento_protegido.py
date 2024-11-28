class Carro:
    def __init__(self, marca: str, modelo: str) -> None:
        self._marca: str = marca
        self._modelo: str = modelo

    def _descricao(self) -> str:
        return f"Este é um carro {self._marca} {self._modelo}."

    def exibir_descricao(self) -> None:
        print(self._descricao())


carro = Carro(marca="Honda", modelo="Civic")
print(carro._marca)
print(carro._descricao())
carro.exibir_descricao()
