"""Exercício 02.

Você está desenvolvendo um sistema de análise de vendas para uma empresa.
Crie um iterador IteradorVendasMensais que percorra uma lista de vendas mensais.
Cada venda é representada como um dicionário contendo informações como mês, valor total
e categoria do produto vendido.
A implementação do método next() deve permitir percorrer as vendas registradas e
retornar a próxima venda na lista.
No entanto, o iterador deve filtrar as vendas apenas para uma categoria específica de
produtos e, se encontrar uma venda com valor total superior a um limite específico,
deve retornar essa venda.
Caso contrário, ele deve pular para a próxima venda até encontrar uma que atenda aos
critérios definidos.
"""
