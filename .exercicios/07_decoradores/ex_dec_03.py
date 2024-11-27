"""Exercício 03.

Você está desenvolvendo um sistema de gerenciamento de pedidos para uma loja.
Você precisa implementar uma funcionalidade que permita calcular o valor total de um
pedido, com a opção de aplicar um desconto se necessário.
Para isso, você decidiu usar um decorador chamado aplicar_desconto, que pode ser
aplicado ao método calcular_total da classe Pedido.

O decorador aplicar_desconto recebe dois parâmetros opcionais: desconto e
valor_desconto.
Se desconto for True, o decorador aplicará o desconto ao valor total do pedido com base
no valor_desconto fornecido.
Caso contrário, o valor total do pedido será calculado sem desconto.

Sua tarefa é implementar o decorador aplicar_desconto e a classe Pedido de acordo com
as especificações fornecidas.
"""
