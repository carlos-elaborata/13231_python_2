"""Exercício 02.

Desenvolva um decorador que registre o horário de início e o tempo de execução de
uma função específica.
O decorador deve salvar essas informações em um arquivo de log, juntamente com o nome
da função, os argumentos recebidos e o resultado retornado.
"""

import logging
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING, TypeVar
from zoneinfo import ZoneInfo

if TYPE_CHECKING:
    from collections.abc import Callable
    from datetime import timedelta
    from logging import Logger

BASE_DIR: Path = Path(__file__).parent

logging.basicConfig(filename=BASE_DIR / "registro_v2.log", level=logging.INFO)

F = TypeVar("F")


def gerar_log(func: "Callable[..., F]") -> "Callable[..., F]":
    def wrapper(*args: object, **kwargs: object) -> F:
        fuso_horario = ZoneInfo(key="America/Sao_Paulo")

        inicio: datetime = datetime.now(tz=fuso_horario)
        logger: Logger = logging.getLogger(name=__name__)
        logger.info(
            "%s: Chamando função '%s' com args: %s, kwargs: %s",
            inicio,
            func.__name__,
            args,
            kwargs,
        )
        resultado: F = func(*args, **kwargs)
        fim: datetime = datetime.now(tz=fuso_horario)
        tempo_execucao: timedelta = fim - inicio

        logger.info("%s: Resultado de '%s': %s.", fim, func.__name__, resultado)
        logger.info(
            "%s: Tempo de execução de '%s': %.5f segundos.",
            fim,
            func.__name__,
            tempo_execucao.total_seconds(),
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
