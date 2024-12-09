import random
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import NoReturn


def contador() -> "Generator[int, None, NoReturn]":
    contador: int = 0
    while True:
        yield contador
        contador += 1


gen_1: "Generator[int, None, NoReturn]" = contador()
gen_2: "Generator[int, None, NoReturn]" = contador()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def exibir_proximos_valores(gen: "Generator[int, None, NoReturn]", n: int) -> None:
    for _ in range(n):
        print(next(gen))


exibir_proximos_valores(gen=gen_1, n=2)
exibir_proximos_valores(gen=gen_2, n=2)
exibir_proximos_valores(gen=gen_1, n=3)
exibir_proximos_valores(gen=gen_2, n=4)


def gerar_temperaturas() -> "Generator[float, None, NoReturn]":
    while True:
        temperatura: float = random.uniform(a=20, b=30)
        yield temperatura
        time.sleep(1)


def processar_temperaturas(
    temperaturas: "Generator[float, None, NoReturn]",
    num_leituras: int,
) -> None:
    soma = 0
    contagem = 0

    for _ in range(num_leituras):
        temperatura: float = next(temperaturas)
        print(f"Temperatura atual: {temperatura:.2f} ºC")
        soma += temperatura
        contagem += 1

    media: float = soma / contagem if contagem > 0 else 0
    print(f"Média das temperaturas: {media:.2f} ºC")


temperaturas: "Generator[float, None, NoReturn]" = gerar_temperaturas()

processar_temperaturas(temperaturas=temperaturas, num_leituras=3)
processar_temperaturas(temperaturas=temperaturas, num_leituras=5)
