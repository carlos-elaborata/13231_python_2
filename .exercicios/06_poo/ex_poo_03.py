"""Exercício 03.

Desenvolva uma classe que represente uma conta bancária com os seguintes atributos:
titular e saldo.
Adicione métodos para realizar operações de depósito e saque na conta.
Certifique-se de tratar casos onde o saldo pode se tornar negativo após um saque.
Após definir a classe, crie uma instância dela e realize algumas operações de depósito
e saque para verificar o funcionamento dos métodos implementados.
"""


class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular: str = titular
        self.saldo: float = saldo

    def depositar(self, valor: float) -> str:
        if valor > 0:
            self.saldo += valor

            return (
                f"\nTitular: {self.titular}\n"
                f"Depósito de R$ {valor:.2f} realizado.\n"
                f"Novo saldo: R$ {self.saldo:.2f}.\n"
            )
        return "Valor do depósito inválido."

    def sacar(self, valor: float) -> str:
        if valor <= 0:
            return "Valor do saque inválido."
        if self.saldo >= valor:
            self.saldo -= valor

            return (
                f"\nTitular: {self.titular}\n"
                f"Saque de R$ {valor:.2f} realizado.\n"
                f"Novo saldo: R$ {self.saldo:.2f}.\n"
            )
        return (
            f"\nTitular: {self.titular}\n"
            f"Tentativa de saque: R$ {valor:.2f}.\n"
            f"Saldo: R$ {self.saldo:.2f}.\n"
            "Saldo insuficiente."
        )


conta_1 = ContaBancaria(titular="João", saldo=1000)
print(conta_1.depositar(valor=500))
print(conta_1.depositar(valor=-42))
print(conta_1.sacar(valor=750))
print(conta_1.sacar(valor=1350))
print(conta_1.sacar(valor=-350))
