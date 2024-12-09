# pyright: reportArgumentType=false

import pytest
from minha_funcao import soma

MSG_TYPE_ERROR = "Os argumentos devem ser números inteiros ou decimais."
MSG_VALUE_ERROR = "Ocorreu um erro ao somar os argumentos."


# def test_soma_basica() -> None:
#     assert soma(3, 5) == 8
#     assert soma(0, 5) == 5
#     assert soma(3, -5) == -2
#     assert soma(5, 0) == 5
#     assert soma(-5, 0) == -5
#     assert soma(-3, -5) == -8
#     assert soma(1000000, 2000000) == 3000000
#     assert soma(10**10, 10**10) == 2 * 10**10
#     assert soma(0.1, 0.2) == pytest.approx(0.3)


@pytest.mark.parametrize(
    ("a", "b", "resultado"),
    [
        (3, 5, 8),
        (0, 5, 5),
        (3, -5, -2),
        (5, 0, 5),
        (-5, 0, -5),
        (-3, -5, -8),
        (1000000, 2000000, 3000000),
        (10**10, 10**10, 2 * 10**10),
        (0.1, 0.2, pytest.approx(expected=0.3)),
    ],
)
def test_soma_basica(a: float, b: float, resultado: float) -> None:
    assert soma(a=a, b=b) == resultado


# def test_soma_tipos_e_excecoes() -> None:
#     with pytest.raises(expected_exception=ValueError, match=MSG_VALUE_ERROR):
#         soma("a", 5)
#     with pytest.raises(expected_exception=ValueError, match=MSG_VALUE_ERROR):
#         soma(3, "b")
#     with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
#         soma(None, 5)
#     with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
#         soma(3, None)


@pytest.mark.parametrize(
    ("a", "b", "erro", "msg"),
    [
        ("a", 5, ValueError, MSG_VALUE_ERROR),
        (3, "b", ValueError, MSG_VALUE_ERROR),
        (None, 5, TypeError, MSG_TYPE_ERROR),
        (3, None, TypeError, MSG_TYPE_ERROR),
    ],
)
def test_soma_tipos_e_excecoes(a: float, b: float, erro: Exception, msg: str) -> None:
    with pytest.raises(erro, match=msg):
        soma(a=a, b=b)
