# pyright: reportArgumentType=false

import pytest
from minha_funcao import soma

MSG_TYPE_ERROR = "Os argumentos devem ser números inteiros ou decimais."
MSG_VALUE_ERROR = "Ocorreu um erro ao somar os argumentos."


def test_soma_basica() -> None:
    assert soma(3, 5) == 8
    assert soma(0, 5) == 5
    assert soma(3, -5) == -2
    assert soma(5, 0) == 5
    assert soma(-5, 0) == -5
    assert soma(-3, -5) == -8
    assert soma(1000000, 2000000) == 3000000
    assert soma(10**10, 10**10) == 2 * 10**10
    assert soma(0.1, 0.2) == pytest.approx(0.3)


def test_soma_tipos_e_excecoes() -> None:
    with pytest.raises(expected_exception=ValueError, match=MSG_VALUE_ERROR):
        soma("a", 5)
    with pytest.raises(expected_exception=ValueError, match=MSG_VALUE_ERROR):
        soma(3, "b")
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        soma(None, 5)
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        soma(3, None)
