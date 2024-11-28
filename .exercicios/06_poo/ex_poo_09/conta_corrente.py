from decimal import Decimal

from conta_bancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, titular: str, saldo: float = 0, limite_extra: float = 0) -> None:
        super().__init__(titular=titular, saldo=saldo)
        self.limite_extra: Decimal = Decimal(value=str(object=limite_extra))

    def sacar(self, valor: float) -> str:
        total_disponivel: Decimal = self.saldo + self.limite_extra
        if 0 < valor <= total_disponivel:
            if valor <= self.saldo:
                self.saldo -= Decimal(value=str(object=valor))
            else:
                valor_excedente: Decimal = Decimal(value=str(object=valor)) - self.saldo
                self.saldo = Decimal(value=0)
                self.limite_extra -= valor_excedente

            return (
                f"\nTitular: {self.titular}\n"
                f"Saque de R$ {valor:.2f} realizado.\n"
                f"Novo saldo: R$ {self.saldo:.2f}.\n"
                f"Limite extra: R$ {self.limite_extra:.2f}.\n"
            )

        return "Erro: Saldo insuficiente ou valor de saque inválido."

    def consultar_saldo(self) -> str:
        return (
            f"\nTitular: {self.titular}\nSaldo: R$ {self.saldo:.2f}.\nLimite extra: "
            f"R$ {self.limite_extra:.2f}"
        )
