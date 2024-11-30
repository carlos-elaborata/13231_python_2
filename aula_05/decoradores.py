from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable

F = TypeVar("F")


def meu_decorador(func: "Callable[..., F]") -> "Callable[..., F]":
    def wrapper(*args: object, **kwargs: object) -> F:
        print("Antes de chamar a função decorada.")
        resultado: object = func(*args, **kwargs)
        print("Depois de chamar a função decorada.")
        return resultado

    return wrapper


@meu_decorador  # É igual a `saudacao = meu_decorador(saudacao)`
def saudacao(nome: str) -> None:
    print(f"Olá, {nome}")


# saudacao(nome="Maria")


@meu_decorador
def multiplicar(a: int, b: int) -> int:
    print(f"Calculando {a} * {b}")
    return a * b


resultado: int = multiplicar(a=5, b=7)
print(f"Resultado da multiplicação: {resultado}")
