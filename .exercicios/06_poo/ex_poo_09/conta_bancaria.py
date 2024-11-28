from decimal import Decimal


class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular: str = titular
        self.saldo: Decimal = Decimal(value=str(object=saldo))

    def trocar_titular(self, novo_titular: str) -> str:
        if not novo_titular:
            return "Erro. O nome do novo titular não pode estar vazio."
        msg_sucesso: str = f"Titular alterado de {self.titular} para {novo_titular}."
        self.titular = novo_titular
        return msg_sucesso

    def depositar(self, valor: float) -> str:
        if valor > 0:
            self.saldo += Decimal(value=str(object=valor))

            return (
                f"\nTitular: {self.titular}\n"
                f"Depósito de R$ {valor:.2f} realizado.\n"
                f"Novo saldo: R$ {self.saldo:.2f}.\n"
            )
        return "Erro: Valor do depósito inválido."

    def sacar(self, valor: float) -> str:
        if 0 < valor <= self.saldo:  # if self.saldo >= valor and valor > 0:
            self.saldo -= Decimal(value=str(object=valor))

            return (
                f"\nTitular: {self.titular}\n"
                f"Saque de R$ {valor:.2f} realizado.\n"
                f"Novo saldo: R$ {self.saldo:.2f}.\n"
            )

        return "Erro: Saldo insuficiente ou valor de saque inválido."

    def consultar_saldo(self) -> str:
        return f"\nTitular: {self.titular}\nSaldo: R$ {self.saldo:.2f}."
