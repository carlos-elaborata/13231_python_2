class Carro:
    def __init__(self, modelo: str, velocidade: int) -> None:
        self.modelo: str = modelo
        self.__velocidade: int = velocidade

    # def get_velocidade(self) -> int:
    #     return self.__velocidade

    # def set_velocidade(self, nova_velocidade: int) -> None:
    #     if nova_velocidade < 0:
    #         msg = "A velocidade não pode ser negativa."
    #         raise ValueError(msg)
    #     self.__velocidade = nova_velocidade

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade: int) -> None:
        if not isinstance(nova_velocidade, int):
            msg = "A velocidade deve ser um número inteiro."
            raise TypeError(msg)
        if nova_velocidade < 0:
            msg = "A velocidade não pode ser negativa."
            raise ValueError(msg)
        self.__velocidade = nova_velocidade

    @velocidade.deleter
    def velocidade(self) -> None:
        self.__velocidade = 0

    def __str__(self) -> str:
        return f"Carro {self.modelo} está a {self.__velocidade} km/h."


carro = Carro(modelo="Toyota", velocidade=80)
print(carro)
# carro.set_velocidade(nova_velocidade=120)
# print(carro.get_velocidade())
carro.velocidade = 120
print(carro.velocidade)
print(carro)
del carro.velocidade
print(carro)
