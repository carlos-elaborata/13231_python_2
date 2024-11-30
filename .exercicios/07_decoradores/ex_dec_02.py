"""Exercício 02.

Desenvolva um decorador que registre o horário de início e o tempo de execução de
uma função específica.
O decorador deve salvar essas informações em um arquivo de log, juntamente com o nome
da função, os argumentos recebidos e o resultado retornado.
"""

import time
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, TypeVar
from zoneinfo import ZoneInfo

if TYPE_CHECKING:
    from collections.abc import Callable
    from datetime import timedelta

# import logging

BASE_DIR: Path = Path(__file__).parent

F = TypeVar("F")


def gerar_log(func: "Callable[..., F]") -> "Callable[..., F]":
    def wrapper(*args: object, **kwargs: object) -> F:
        fuso_horario = ZoneInfo(key="America/Sao_Paulo")

        inicio: datetime = datetime.now(tz=fuso_horario)
        resultado: F = func(*args, **kwargs)
        fim: datetime = datetime.now(tz=fuso_horario)
        tempo_execucao: timedelta = fim - inicio

        with Path(BASE_DIR / "registro.log").open(mode="a", encoding="utf8") as arq_log:
            arq_log.write(
                f"{inicio}: Chamada de '{func.__name__}' com args: {args}, kwargs: "
                f"{kwargs}.\n"
                f"{fim}: Resultado de '{func.__name__}': {resultado}.\n"
                f"{fim}: Tempo de execução de '{func.__name__}': "
                f"{tempo_execucao.total_seconds():.5f} segundos.\n",
            )

        return resultado

    return wrapper


@gerar_log
def soma(a: int, b: int) -> int:  # noqa: FURB118
    return a + b


@gerar_log
def dormir(
    *args: object,
    **kwargs: object,
) -> tuple[tuple[object, ...], dict[str, object]]:
    time.sleep(2)
    return args, kwargs


resultado: int = soma(3, 5)
print(f"Resultado da soma: {resultado}")
print(dormir("A", 1, teste_1=5.5, x="Batman", y=False))
