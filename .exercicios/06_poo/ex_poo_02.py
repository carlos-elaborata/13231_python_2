"""Exercício 02.

Desenvolva uma classe chamada Calculadora que simule as operações básicas de uma
calculadora.
A classe deve conter métodos para adição, subtração, multiplicação e divisão.
Crie uma instância da classe Calculadora e realize algumas operações matemáticas
utilizando os métodos implementados.
    Exemplo de operações esperadas:
        5 + 3 = 8
        10 - 4 = 6
        2 * 6 = 12
        8 / 2 = 4.0
"""


class Calculadora:
    @staticmethod
    def adicao(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtracao(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplicacao(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divisao(a: float, b: float) -> float | str:
        if b != 0:
            return a / b
        return "Impossível dividir por zero."


print(f"5 + 3 = {Calculadora.adicao(5, 3)}")
print(f"10 - 4 = {Calculadora.subtracao(10, 4)}")
print(f"2 * 6 = {Calculadora.multiplicacao(2, 6)}")
print(f"8 / 2 = {Calculadora.divisao(8, 2)}")
print(f"5 / 0 = {Calculadora.divisao(5, 0)}")
