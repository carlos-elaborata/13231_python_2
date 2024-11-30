from decimal import Decimal


class ContaBancaria:
    def __init__(self, numero: int, titular: str, saldo: Decimal) -> None:
        self.numero: int = numero
        self.titular: str = titular
        self.saldo: Decimal = saldo

    def depositar(self, valor: Decimal) -> str:
        if valor > 0:
            self.saldo += valor

            return (
                f"Depósito de R$ {valor:.2f} realizado com sucesso."
                f"Saldo atual: R$ {self.saldo:.2f}"
            )

        return "Erro: O valor do depósito deve ser maior do que zero."

    def sacar(self, valor: Decimal) -> str:
        if 0 < valor <= self.saldo:
            self.saldo -= valor

            return (
                f"Saque de R$ {valor:.2f} realizado com sucesso."
                f"Saldo atual: R$ {self.saldo:.2f}"
            )

        return "Erro: Saldo insuficiente ou valor inválido para saque."

    def __str__(self) -> str:
        return f"Conta: {self.numero} de {self.titular}: R$ {self.saldo:.2f}."

    def get_info(self) -> str:
        return f"Olá {self.titular}, seu saldo atual é de R$ {self.saldo:.2f}."
