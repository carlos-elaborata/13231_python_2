from types import NotImplementedType


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

    def __getitem__(self, key: int) -> str:
        return self.titular[key]

    def __setitem__(self, key: int, value: str) -> None:
        temp = list(self.titular)
        temp[key] = value
        self.titular = "".join(temp)
        print(f"Nome do titular alterado para {self.titular}.")

    def __delitem__(self, key: int) -> None:
        temp = list(self.titular)
        del temp[key]
        self.titular = "".join(temp)
        print(f"Nome do titular alterado para {self.titular}.")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ContaBancaria):
            return self.saldo == other.saldo
        return False

    def __ne__(self, other: object) -> bool:
        if isinstance(other, ContaBancaria):
            return self.saldo != other.saldo
        return True

    def __gt__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, ContaBancaria):
            return self.saldo > other.saldo
        return NotImplemented

    def __lt__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, ContaBancaria):
            return self.saldo < other.saldo
        return NotImplemented

    def __ge__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, ContaBancaria):
            return self.saldo >= other.saldo
        return NotImplemented

    def __le__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, ContaBancaria):
            return self.saldo <= other.saldo
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.titular, self.saldo))


conta_1 = ContaBancaria(titular="João", saldo=1000)
conta_2 = ContaBancaria(titular="Maria", saldo=500)
# del conta_bancaria

print("\nUsando __str__ e __repr__:")
print(f"Representação amigável de `conta_1` (__str__):\n{conta_1!s}\n")
print(f"Representação oficial de `conta_1` (__repr__):\n{conta_1!r}\n")

print(conta_1[0])
conta_1[0] = "L"
del conta_1[0]

print("\nComparando contas com __eq__ e __ne__:")
print(f"conta_1 == conta_2? {conta_1 == conta_2}")
print(f"conta_1 != conta_2? {conta_1 != conta_2}")

print("\nComparando saldos com operadores relacionais:")
print(f"conta_1 > conta_2? {conta_1 > conta_2}")
print(f"conta_1 < conta_2? {conta_1 < conta_2}")
print(f"conta_1 >= conta_2? {conta_1 >= conta_2}")
print(f"conta_1 <= conta_2? {conta_1 <= conta_2}")

contas_set: set[ContaBancaria] = {conta_1, conta_2}
print(f"Conjunto das contas: {contas_set}")
