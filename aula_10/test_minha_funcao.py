from minha_funcao import soma


def test_soma_basica() -> None:
    assert soma(3, 5) == 8
    assert soma(0, 5) == 5
    assert soma(3, -5) == -2
