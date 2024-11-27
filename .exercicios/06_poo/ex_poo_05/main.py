from produtos import Produto

produto_1 = Produto(nome="Camiseta", preco=29.99, estoque=50)
produto_2 = Produto(nome="Calça Jeans", preco=59.99, estoque=30)

print(produto_1.descricao())
print(produto_2.descricao())

produto_1.aumentar_estoque(quantidade=20)
produto_2.diminuir_estoque(quantidade=10)

print(produto_1.descricao())
print(produto_2.descricao())

print("\nValor total do estoque:")
print(f"Produto 1: R$ {produto_1.calcular_valor_total():.2f}")
print(f"Produto 2: R$ {produto_2.calcular_valor_total():.2f}")

print(produto_1.calcular_valor_total())
print(produto_2.calcular_valor_total())
