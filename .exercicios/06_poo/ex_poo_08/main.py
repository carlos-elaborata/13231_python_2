from conta_bancaria import ContaBancaria

conta_bancaria = ContaBancaria(titular="João", saldo=1000)

print(conta_bancaria.get_info())

print(conta_bancaria.depositar(valor=500))
print(conta_bancaria.sacar(valor=2000))
print(conta_bancaria.sacar(valor=1000))

print(conta_bancaria.set_titular(novo_titular="Maria"))

print(conta_bancaria.get_info())
