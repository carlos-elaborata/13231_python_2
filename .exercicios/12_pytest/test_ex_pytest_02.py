# pyright: reportArgumentType=false

import pytest
from ex_pytest_02 import calcular_media


@pytest.mark.parametrize(
    ("valores", "resultado"),
    [
        ([1, 2, 3, 4, 5], 3),
        ([-1, -2, -3, -4, -5], -3),
        ([-1, 2, -3, 4, -5], -0.6),
        ([], 0),
        ([1.5, 2.5, 3.5, 4.5, 5.5], 3.5),
        ([0, 0, 0, 0, 0], 0),
        ([42], 42),
        ([1e18, -1e18], 0),
    ],
)
def test_calcular_media(valores: list[float], resultado: float) -> None:
    assert calcular_media(valores=valores) == resultado


def test_calcular_media_lista_grande() -> None:
    valores: list[int] = list(range(10000))
    resultado: float = sum(valores) / len(valores)
    assert calcular_media(valores=valores) == resultado


@pytest.mark.parametrize(
    ("valores", "erro", "msg"),
    [
        (["a", "b", "c"], TypeError, "Todos os valores devem ser números."),
        ([1, 2, 3, 4, "a"], TypeError, "Todos os valores devem ser números."),
        (["1", "2", "3"], TypeError, "Todos os valores devem ser números."),
        ({"a": 1, "b": 2}, TypeError, "A entrada deve ser uma lista."),
        ((1, 2, 3), TypeError, "A entrada deve ser uma lista."),
        ({1, 2, 3}, TypeError, "A entrada deve ser uma lista."),
        (None, TypeError, "A entrada deve ser uma lista."),
    ],
)
def test_calcular_media_valores_invalidos(
    valores: list[str | int] | dict[str, int] | tuple[int, ...] | set[int] | None,
    erro: type[Exception],
    msg: str,
) -> None:
    with pytest.raises(expected_exception=erro, match=msg):
        calcular_media(valores=valores)
