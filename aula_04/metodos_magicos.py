class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular: str = titular
        self.saldo: float = saldo
        print(
            f"Conta criada para {self.titular} com saldo inicial de {self.saldo:.2f}.",
        )

    # def __del__(self) -> None:
    #     print(f"A conta de {self.titular} foi encerrada.")

    def __str__(self) -> str:
        return f"Conta de {self.titular} com saldo de {self.saldo:.2f}."

    def __repr__(self) -> str:
        return f"ContaBancaria(titular='{self.titular}', saldo={self.saldo})"

    def __len__(self) -> int:
        return len(self.titular)


conta_bancaria = ContaBancaria(titular="João", saldo=1000)
# del conta_bancaria
print(conta_bancaria)
print(repr(conta_bancaria))
print(len(conta_bancaria))
