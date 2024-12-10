from produto import Produto
from venda import Venda

produto_1 = Produto(nome="Laptop", preco=2500, estoque=10)
produto_2 = Produto(nome="Mouse", preco=25, estoque=50)

print("Estoque inicial:")
print(produto_1)
print(produto_2)

venda_1 = Venda(produto=produto_1, quantidade=2)
venda_2 = Venda(produto=produto_2, quantidade=5)

print("\nVendas realizadas:")
print(venda_1)
print(venda_2)

print("\nEstoque após as vendas:")
print(produto_1)
print(produto_2)
