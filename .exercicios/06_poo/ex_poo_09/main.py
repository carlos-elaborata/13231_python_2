from conta_bancaria import ContaBancaria
from conta_corrente import ContaCorrente

conta_bancaria = ContaBancaria(titular="João", saldo=1000)
conta_corrente = ContaCorrente(titular="Maria", saldo=2000, limite_extra=500)

print(conta_bancaria.consultar_saldo())
print(conta_bancaria.depositar(valor=500))
print(conta_bancaria.sacar(valor=200))
print(conta_bancaria.consultar_saldo())

print(conta_corrente.consultar_saldo())
print(conta_corrente.depositar(valor=1000))
print(conta_corrente.sacar(valor=3200))
print(conta_corrente.consultar_saldo())

conta_bancaria.trocar_titular(novo_titular="Anna")
print(conta_bancaria.consultar_saldo())
