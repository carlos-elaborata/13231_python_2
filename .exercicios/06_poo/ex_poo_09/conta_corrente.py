from decimal import Decimal

from conta_bancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, titular: str, saldo: float = 0, limite_extra: float = 0) -> None:
        super().__init__(titular=titular, saldo=saldo)
        self.limite_extra: Decimal = Decimal(value=str(object=limite_extra))

    def sacar(self, valor: float):
        pass

    def consultar_saldo(self) -> str:
        return (
            f"\nTitular: {self.titular}\nSaldo: R$ {self.saldo:.2f}.\nLimite extra: "
            f"R$ {self.limite_extra:.2f}"
        )
