from decimal import Decimal

from conta_bancaria import ContaBancaria

conta = ContaBancaria(numero=1234, titular="João", saldo=Decimal(value="1000.00"))

print(conta)
print(conta.get_info())
