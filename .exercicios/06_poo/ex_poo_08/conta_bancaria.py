from decimal import Decimal


class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.__titular: str = titular
        self.__saldo: Decimal = Decimal(value=str(object=saldo))

    def get_saldo(self) -> Decimal:
        return self.__saldo

    def get_titular(self) -> str:
        return self.__titular

    def set_titular(self, novo_titular: str) -> str:
        if novo_titular:
            self.__titular = novo_titular

            return f"Titular da conta alterado para {self.__titular}"

        return "O nome do titular não pode estar em branco."

    def get_info(self) -> str:
        return f"Titular: {self.__titular}\nSaldo: R$ {self.__saldo:.2f}."

    def depositar(self, valor: float) -> str:
        if valor > 0:
            self.__saldo += Decimal(value=str(object=valor))

            return (
                f"Depósito de R$ {valor:.2f} realizado com sucesso.\n"
                f"Novo saldo: R$ {self.__saldo:.2f}."
            )

        return "Valor de depósito inválido."

    def sacar(self, valor: float) -> str:
        if 0 < valor <= self.__saldo:
            self.__saldo -= Decimal(value=str(object=valor))

            return (
                f"Saque de R$ {valor:.2f} realizado com sucesso.\n"
                f"Novo saldo: R$ {self.__saldo:.2f}."
            )

        return "Saldo insuficiente ou valor de saque inválido."
