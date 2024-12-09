class Carro:
    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca: str = marca
        self.__modelo: str = modelo

    def get_marca(self) -> str:
        return self.__marca

    def set_marca(self, nova_marca: str) -> None:
        if nova_marca:
            self.__marca = nova_marca

    def __descricao(self) -> str:
        return f"Este é um carro {self.__marca} {self.__modelo}."

    def exibir_descricao(self) -> None:
        print(self.__descricao())


carro = Carro(marca="Honda", modelo="Civic")
# print(carro.__marca)
# print(carro.__descricao())
carro.exibir_descricao()
# carro.set_marca(nova_marca="Toyota")
carro.__marca = "VW"
carro._Carro__marca = "Toyota"
print(carro.__dict__)
carro.exibir_descricao()

a = {"_Carro__marca": "Toyota", "_Carro__modelo": "Civic", "__marca": "VW"}
